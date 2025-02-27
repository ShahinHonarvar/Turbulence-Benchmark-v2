import itertools

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[3:9] if c.isalpha())).lower()
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            candidate = ''.join(combination)
            if candidate == candidate[::-1] and len(candidate) >= 7:
                palindromes.add(candidate)
    return palindromes