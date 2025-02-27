from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:9].lower()
    chars = [c for c in s if s.count(c) >= 2]
    chars = set(chars)
    palindromes = set()
    for i in range(3, len(s) // 2 + 2):
        for p in permutations(s, i):
            p = ''.join(p)
            if p == p[::-1] and len(p) >= 7:
                palindromes.add(p)
    return palindromes