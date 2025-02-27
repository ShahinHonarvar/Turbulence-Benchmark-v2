import itertools

def palindromes_between_indices(s):
    s = s[4:10].lower()
    palindromes = set()
    for i in range(6, len(s) + 1):
        for p in itertools.permutations(s, i):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes