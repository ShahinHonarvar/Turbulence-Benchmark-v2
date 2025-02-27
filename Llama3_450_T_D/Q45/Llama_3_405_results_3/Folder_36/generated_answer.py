import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[5:9])).lower()
    if len(s) < 3:
        return set()
    palindromes = set()
    for r in range(3, len(s) + 1):
        for p in itertools.permutations(s, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes