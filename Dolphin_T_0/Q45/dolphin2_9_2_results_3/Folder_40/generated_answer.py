from itertools import permutations
    import string

def palindromes_between_indices(s):
    s = s[4:10]
    palindromes = set()
    for p in permutations(s, 7):
        p = ''.join(p)
        if p.lower() == p.lower()[::-1]:
            palindromes.add(p.lower())
    return palindromes if len(palindromes) > 0 else set()