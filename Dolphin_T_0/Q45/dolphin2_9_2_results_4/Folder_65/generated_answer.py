from itertools import combinations

def palindromes_between_indices(s):
    letters = ''.join(sorted(s[0:7]))
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for c in combinations(letters, i):
            s = ''.join(c)
            if s.lower() == s.lower()[::-1]:
                palindromes.add(s.lower())
    return palindromes