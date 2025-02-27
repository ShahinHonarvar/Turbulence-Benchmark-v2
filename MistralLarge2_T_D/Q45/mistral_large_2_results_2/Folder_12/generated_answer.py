import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[3:9])
    letters = ''.join(letters).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, prefix=''):
        if len(prefix) >= 4 and is_palindrome(prefix):
            palindromes.add(prefix)
        for char in chars:
            generate_palindromes(chars - {char}, prefix + char)
    generate_palindromes(set(letters))
    return palindromes