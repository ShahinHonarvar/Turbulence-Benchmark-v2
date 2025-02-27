import itertools

def palindromes_between_indices(s):
    s = s[1:7].lower()
    palindromes = set()
    for i in range(7, 13):
        for p in itertools.permutations(s, i):
            if len(p) >= 7 and p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes