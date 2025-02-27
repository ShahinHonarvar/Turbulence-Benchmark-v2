from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    palindromes = set()
    for p in permutations(s, len(s)):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 4:
            palindromes.add(p)
    return palindromes