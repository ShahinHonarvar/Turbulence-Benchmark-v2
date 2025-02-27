import itertools

def palindromes_between_indices(s):
    s = s[3:6].lower()
    s = ''.join(filter(str.isalpha, s))
    result = set()
    for r in range(3, len(s) + 1):
        for p in itertools.permutations(s, r):
            p = ''.join(p)
            if p == p[::-1]:
                result.add(p)
    return result