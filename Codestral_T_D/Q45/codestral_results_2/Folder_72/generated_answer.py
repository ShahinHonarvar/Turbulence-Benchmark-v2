from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[1:8]
    palindromes = set()
    for p in permutations(s, 6):
        if p == p[::-1]:
            palindromes.add(''.join(p))
    return palindromes