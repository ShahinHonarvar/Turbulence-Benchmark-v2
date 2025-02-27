from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6]
    palindromes = set()
    for p in permutations(s, len(s)):
        p = ''.join(p)
        if p.lower() == p[::-1].lower():
            if len(p) >= 5:
                palindromes.add(p)
    return palindromes