import re

def palindrome_of_length_at_least_n(string):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 33, len(string) + 1):
            word = string[i:j]
            if is_palindrome(word) and bool(re.fullmatch('[a-zA-Z]+', word)):
                palindromes.add(word)
    return palindromes