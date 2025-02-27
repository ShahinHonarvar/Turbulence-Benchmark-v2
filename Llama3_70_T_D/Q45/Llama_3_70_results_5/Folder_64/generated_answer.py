from itertools import combinations, permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for p in combinations(letters, 5):
        for q in permutations(p):
            q = ''.join(q)
            if q == q[::-1]:
                palindromes.add(q)
    for p in combinations(letters, 6):
        for q in permutations(p):
            q = ''.join(q)
            if q == q[::-1]:
                palindromes.add(q)
    return palindromes