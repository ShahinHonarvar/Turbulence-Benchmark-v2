from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def get_palindromes(letters):
        palindromes = set()
        for r in range(3, len(letters) + 1):
            for perm in permutations(letters, r):
                word = ''.join(perm)
                if is_palindrome(word.lower()):
                    palindromes.add(word.lower())
        return palindromes
    letters = [c for c in s[1:3].lower() if c.isalpha()]
    return get_palindromes(letters)