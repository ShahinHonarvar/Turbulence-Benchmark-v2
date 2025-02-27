from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[4:9].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 6 and is_palindrome(word):
            palindromes.add(word)
    return palindromes