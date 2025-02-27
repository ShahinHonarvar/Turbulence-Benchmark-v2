from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    potential_chars = [char.lower() for char in s[3:9] if char.isalpha()]
    potential_palindromes = set()
    for perm in permutations(potential_chars):
        word = ''.join(perm)
        if len(word) >= 4 and is_palindrome(word):
            potential_palindromes.add(word)
    valid_palindromes = {p for p in potential_palindromes if len(p) >= 4}
    return valid_palindromes