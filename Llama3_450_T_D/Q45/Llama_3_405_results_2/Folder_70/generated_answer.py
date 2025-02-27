from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:7] if c.isalpha()]
    unique_letters = set((letter.lower() for letter in letters))
    palindromes = set()
    for r in range(2, len(unique_letters) + 1):
        for perm in permutations(unique_letters, r):
            palindrome = ''.join(perm) + ''.join(perm[::-1])
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes