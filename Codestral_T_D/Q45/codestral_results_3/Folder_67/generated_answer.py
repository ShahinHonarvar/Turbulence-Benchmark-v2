import itertools

def palindromes_between_indices(s):
    s = s[2:7].lower()
    palindromes = set()
    for i in range(5, len(s) + 1):
        for p in itertools.permutations(s, i):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes