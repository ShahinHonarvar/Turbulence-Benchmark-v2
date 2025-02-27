from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[5:10] if c.isalpha()]
    letters_lower = [c.lower() for c in letters]
    all_permutations = set((''.join(p) for p in permutations(letters_lower, len(letters_lower))))
    palindromes = {p for p in all_permutations if is_palindrome(p) and len(p) >= 5}
    return palindromes