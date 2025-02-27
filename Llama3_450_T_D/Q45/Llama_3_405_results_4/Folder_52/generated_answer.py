from itertools import combinations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:8] if c.isalpha()]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for combo in combinations(letters, r):
            palindrome = ''.join(combo) + ''.join(combo[::-1])
            palindromes.add(palindrome)
    return palindromes