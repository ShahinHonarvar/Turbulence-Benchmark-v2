from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        for perm in permutations(letters, 7):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word.lower())
        return palindromes
    letters = [c.lower() for c in s[0:8] if c.isalpha()]
    if len(letters) < 7:
        return set()
    return generate_palindromes(letters)