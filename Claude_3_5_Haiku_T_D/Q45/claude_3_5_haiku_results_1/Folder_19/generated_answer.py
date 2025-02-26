from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        unique_pals = set()
        for perm in set(permutations(letters)):
            word = ''.join(perm).lower()
            if is_palindrome(word) and len(word) >= 7:
                unique_pals.add(word)
        return unique_pals
    letters = [char for char in s[1:8] if char.isalpha()]
    return generate_palindromes(letters)