import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:5] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combo in itertools.permutations(letters, r):
            combo = ''.join(combo)
            if combo == combo[::-1]:
                palindromes.add(combo)
    return palindromes