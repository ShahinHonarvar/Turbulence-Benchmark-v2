import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    return palindromes