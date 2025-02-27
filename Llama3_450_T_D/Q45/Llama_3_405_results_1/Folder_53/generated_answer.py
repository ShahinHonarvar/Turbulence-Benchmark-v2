import itertools

def palindromes_between_indices(s):
    s = s[4:9]
    s = ''.join(filter(str.isalpha, s)).lower()
    letters = set(s)
    palindromes = set()
    for r in range(3, len(s) + 1):
        for perm in itertools.permutations(letters, r):
            p = ''.join(perm)
            if p == p[::-1] and len(p) >= 6:
                palindromes.add(p)
    return palindromes