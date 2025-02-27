import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:7] if c.isalpha() and c.isascii()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combination in itertools.permutations(letters, r):
            p = ''.join(combination)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes