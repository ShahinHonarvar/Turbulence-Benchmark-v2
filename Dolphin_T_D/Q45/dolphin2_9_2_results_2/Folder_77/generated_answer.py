import itertools

def palindromes_between_indices(s):
    s = s[4:7]
    palindromes = set()
    for length in range(4, len(s) + 1):
        for perm in itertools.permutations(s, length):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p.lower())
    return palindromes