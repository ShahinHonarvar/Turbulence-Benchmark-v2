from itertools import permutations

def palindromes_between_indices(s):
    palette = [c.lower() for c in s[1:4]]
    palindromes = set()
    for p in permutations(palette, 4):
        s = ''.join(p)
        if s == s[::-1]:
            palindromes.add(s)
    return palindromes