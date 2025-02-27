import itertools

def palindromes_between_indices(s):
    s = s[4:10].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(4, len(s) + 1):
        for perm in itertools.permutations(s, r):
            perm = ''.join(perm)
            if perm == perm[::-1]:
                palindromes.add(perm)
    return palindromes