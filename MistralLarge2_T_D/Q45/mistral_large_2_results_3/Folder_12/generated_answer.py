from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [char for char in s[3:9] if char.isalpha()]
    all_permutations = set((''.join(p).lower() for p in permutations(letters)))
    palindromes = {p for p in all_permutations if is_palindrome(p) and len(p) >= 4}
    return palindromes