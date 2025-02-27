import itertools

def palindromes_between_indices(s):
    s = s[4:10]
    s = ''.join(filter(str.isalpha, s)).lower()
    if len(s) < 3:
        return set()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in itertools.permutations(s, i):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes