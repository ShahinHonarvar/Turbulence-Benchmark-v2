from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join(filter(str.isalpha, s[1:6].lower()))
    palindromes = {word for word in map(''.join, permutations(substring, len(substring))) if is_palindrome(word) and len(word) >= 4}
    return palindromes