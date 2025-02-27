from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for r in range(5, len(s) + 1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes