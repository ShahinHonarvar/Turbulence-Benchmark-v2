from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            p = ''.join(p)
            if p == p[::-1] and len(p) >= 6:
                palindromes.add(p)
    return palindromes