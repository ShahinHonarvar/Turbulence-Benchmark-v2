from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    letters = [c.lower() for c in s[2:10] if c.isalpha()]
    return {''.join(p) for p in permutations(letters, 4) if is_palindrome(p)}