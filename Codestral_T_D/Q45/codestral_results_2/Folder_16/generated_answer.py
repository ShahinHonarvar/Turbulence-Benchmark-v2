from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:10].lower()
    palindromes = set()
    for p in permutations(s):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 5:
            palindromes.add(p)
    return palindromes