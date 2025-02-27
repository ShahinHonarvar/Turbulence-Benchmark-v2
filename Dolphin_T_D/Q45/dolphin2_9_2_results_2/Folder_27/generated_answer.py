from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9]
    palindromes = set()
    for p in permutations(s):
        p = ''.join(p)
        if len(p) >= 6 and p.lower() == p[::-1].lower():
            palindromes.add(p)
    return palindromes