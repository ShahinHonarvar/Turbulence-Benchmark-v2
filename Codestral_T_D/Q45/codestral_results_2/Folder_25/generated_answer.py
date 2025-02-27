from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:5].lower()
    palindromes = set()
    for p in permutations(s, len(s)):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 3:
            palindromes.add(p)
    return palindromes