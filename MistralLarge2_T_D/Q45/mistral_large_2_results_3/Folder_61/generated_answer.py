from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[:8])).lower()
    palindromes = {''.join(p) for i in range(7, len(letters) + 1) for p in permutations(letters, i) if is_palindrome(p)}
    return palindromes