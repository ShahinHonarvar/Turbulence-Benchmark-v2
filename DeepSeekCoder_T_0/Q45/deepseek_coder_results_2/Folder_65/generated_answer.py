from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        for perm in permutations(letters):
            word = ''.join(perm)
            if is_palindrome(word) and len(word) >= 5:
                palindromes.add(word.lower())
        return palindromes
    letters = [c.lower() for c in s[0:7] if c.isalpha()]
    return generate_palindromes(letters)