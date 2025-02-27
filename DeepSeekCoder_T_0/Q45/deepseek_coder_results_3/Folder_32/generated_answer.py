from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        for perm in permutations(letters, len(letters)):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word.lower())
        return palindromes
    letters = [char.lower() for char in s[1:8] if char.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = generate_palindromes(letters)
    return {p for p in palindromes if len(p) >= 5}