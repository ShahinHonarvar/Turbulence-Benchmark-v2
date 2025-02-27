from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    palindromes = set()
    for p in permutations(s):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 4:
            palindromes.add(p)
    return palindromes