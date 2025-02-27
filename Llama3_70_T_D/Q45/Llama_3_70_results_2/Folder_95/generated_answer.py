import itertools

def palindromes_between_indices(s):
    s = s[7:9].lower()
    palindromes = set()
    for r in range(3, len(s) + 1):
        for p in set(itertools.permutations(s, r)):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes