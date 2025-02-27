from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def get_palindromes(letters):
        palindromes = set()
        for perm in permutations(letters, 7):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word.lower())
        return palindromes
    letters = [c.lower() for c in s[0:7] if c.isalpha()]
    if len(letters) < 7:
        return set()
    return get_palindromes(letters)