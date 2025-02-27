import itertools

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[4:10])).lower()
    if len(s) < 3:
        return set()
    palindromes = set()
    for r in range(3, len(s) + 1):
        for perm in itertools.permutations(s, r):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes