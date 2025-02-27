from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:6].lower()))
    letters = Counter(s)
    palindromes = set()
    for r in range(4, len(s) + 1):
        for perm in permutations(s, r):
            p = ''.join(perm)
            if p == p[::-1] and Counter(p) <= letters:
                palindromes.add(p)
    return palindromes