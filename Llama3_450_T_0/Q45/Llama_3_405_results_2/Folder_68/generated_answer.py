import itertools

def palindromes_between_indices(s):
    s = s[1:9].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(4, len(s) + 1):
        for perm in itertools.permutations(s, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes