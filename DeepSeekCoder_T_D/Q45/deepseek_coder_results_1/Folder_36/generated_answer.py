from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def get_palindromes(letters):
        palindromes = set()
        for i in range(3, len(letters) + 1):
            for perm in permutations(letters, i):
                word = ''.join(perm)
                if is_palindrome(word.lower()):
                    palindromes.add(word.lower())
        return palindromes
    letters = [c.lower() for c in s[5:9] if c.isalpha()]
    return get_palindromes(letters)