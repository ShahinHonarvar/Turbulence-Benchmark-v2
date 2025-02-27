import itertools

def palindromes_between_indices(s):
    s = ''.join((c for c in s[6:10] if c.isalpha())).lower()
    letters = sorted(set(s))
    palindromes = set()
    for r in range(4, len(s) + 1):
        for p in itertools.product(letters, repeat=r):
            p = ''.join(p)
            if p == p[::-1] and all((p.count(c) <= s.count(c) for c in p)):
                palindromes.add(p)
    return palindromes