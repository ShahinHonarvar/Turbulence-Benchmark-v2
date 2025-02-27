from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    palindromes = set()
    for p in permutations(s):
        w = ''.join(p)
        if w == w[::-1] and len(w) >= 5:
            palindromes.add(w)
    return palindromes