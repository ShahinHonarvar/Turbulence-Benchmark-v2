from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(3, len(s) + 1):
        for perm in permutations(s, r):
            perm = ''.join(perm)
            if perm == perm[::-1] and all((counter[c] >= perm.count(c) for c in set(perm))):
                palindromes.add(perm)
    return palindromes