import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:3] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combo in itertools.permutations(letters, length):
            if combo == combo[::-1]:
                palindromes.add(''.join(combo))
    return palindromes