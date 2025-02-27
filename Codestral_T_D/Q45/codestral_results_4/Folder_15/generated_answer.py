from itertools import combinations

def palindromes_between_indices(s):
    s = s[1:3].lower()
    palindromes = set()
    for r in range(3, len(s) + 1):
        for c in combinations(s, r):
            c = ''.join(c)
            if c == c[::-1]:
                palindromes.add(c)
    return palindromes