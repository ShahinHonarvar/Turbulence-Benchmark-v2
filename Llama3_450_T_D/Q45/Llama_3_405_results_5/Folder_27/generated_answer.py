from itertools import combinations, permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    letters_set = set(letters)
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combo in combinations(letters, r):
            for perm in permutations(combo):
                p = ''.join(perm)
                if p == p[::-1]:
                    palindromes.add(p)
    return palindromes