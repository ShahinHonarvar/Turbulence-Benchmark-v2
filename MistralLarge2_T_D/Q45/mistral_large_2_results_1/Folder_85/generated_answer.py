from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[2:9] if c.isalpha()]
    all_permutations = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = {p for p in all_permutations if is_palindrome(p) and len(p) >= 7}
    return palindromes