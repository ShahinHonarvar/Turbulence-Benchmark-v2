from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8].lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for r in range(7, len(s) + 1):
        for perm in permutations(s, r):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes