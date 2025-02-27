from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def get_palindromes(letters):
        palindromes = set()
        for perm in permutations(letters, 6):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
        return palindromes
    letters = ''.join(filter(str.isalpha, s[0:7])).lower()
    return get_palindromes(letters) if len(letters) >= 6 else set()