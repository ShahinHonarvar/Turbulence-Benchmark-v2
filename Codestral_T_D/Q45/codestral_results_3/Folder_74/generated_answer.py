import itertools

def palindromes_between_indices(s):
    s = s[1:7].lower()
    palindromes = set()
    for i in range(6, 1, -1):
        for p in itertools.permutations(s, i):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes