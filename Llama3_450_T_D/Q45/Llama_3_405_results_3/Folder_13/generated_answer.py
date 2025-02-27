import itertools

def palindromes_between_indices(s):
    s = s[3:10].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(5, len(s) + 1):
        for perm in itertools.permutations(s, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes