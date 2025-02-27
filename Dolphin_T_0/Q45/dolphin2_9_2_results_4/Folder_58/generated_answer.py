from itertools import permutations

def palindromes_between_indices(s):
    if len(s) != 7:
        return set()
    s = ''.join(filter(str.isalpha, s)).lower()
    permuts = [''.join(p) for p in permutations(s)]
    palindromes = set()
    for p in permuts:
        if len(p) >= 6 and p == p[::-1]:
            palindromes.add(p)
    return palindromes