from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[5:10] if c.isalpha()]
    letter_set = set((c.lower() for c in letters))
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for perm in permutations(letters, r):
            perm_lower = [c.lower() for c in perm]
            if len(perm_lower) >= 6 and perm_lower == perm_lower[::-1]:
                palindrome = ''.join(perm_lower)
                palindromes.add(palindrome)
    return palindromes