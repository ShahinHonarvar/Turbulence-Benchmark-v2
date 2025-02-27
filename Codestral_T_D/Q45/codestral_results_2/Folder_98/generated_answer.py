import itertools

def palindromes_between_indices(s):
    s = s[3:6].lower()
    palindromes = set()
    for r in range(4, len(s) + 1):
        for p in itertools.permutations(s, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes