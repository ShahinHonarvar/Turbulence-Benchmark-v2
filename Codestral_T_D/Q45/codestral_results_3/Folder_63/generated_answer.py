from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:4].lower()
    palindromes = set()
    for p in permutations(s):
        w = ''.join(p)
        if w == w[::-1] and len(w) >= 3:
            palindromes.add(w)
    return palindromes