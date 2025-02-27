from itertools import combinations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    palindromes = set()
    for r in range(6, len(s) + 1):
        for c in combinations(s, r):
            if c == c[::-1]:
                palindromes.add(''.join(c))
    return palindromes