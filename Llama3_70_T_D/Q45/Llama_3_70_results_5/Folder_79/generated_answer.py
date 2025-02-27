from itertools import combinations

def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[1:8] if c.isalpha()))
    palindromes = set()
    for length in range(3, 9):
        for combo in combinations(letters, length // 2 + length % 2):
            middle_char = '' if length % 2 == 0 else combo[-1]
            palindrome = ''.join(combo + (middle_char,) + combo[::-1])
            palindromes.add(palindrome)
    return palindromes