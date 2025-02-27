from itertools import permutations

def palindromes_between_indices(s):
    sub = s[1:7]
    palindromes = set()
    for p in permutations(sub, len(sub)):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 6:
            palindromes.add(p.lower())
    return palindromes