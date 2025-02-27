import itertools

def palindromes_between_indices(s):
    s = s[1:9].lower()
    s = ''.join(filter(str.isalpha, s))
    if len(s) < 7:
        return set()
    palindromes = set()
    for r in range(7, len(s) + 1):
        for p in itertools.permutations(s, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes