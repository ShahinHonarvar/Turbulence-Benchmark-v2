from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = [c for c in s[3:8] if c.isalpha()]
    palindromes = set((word for word in map(''.join, permutations(letters, len(letters))) if len(word) >= 4 and is_palindrome(word)))
    return palindromes