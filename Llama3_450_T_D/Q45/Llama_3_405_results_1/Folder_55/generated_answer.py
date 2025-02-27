from itertools import combinations, permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:3] if c.isalpha()]
    if len(letters) < 3:
        return set()
    letters_set = set(letters)
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for comb in combinations(letters_set, r):
            for perm in permutations(comb):
                palindrome = ''.join(perm) + ''.join(perm[:-1][::-1])
                palindromes.add(palindrome)
    return palindromes