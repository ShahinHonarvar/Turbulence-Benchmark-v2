import re

def palindromes_between_indices(s):
    letters = re.findall('[a-z]', s[1:5], re.IGNORECASE)
    letters = ''.join(letters).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters, current='', length=4):
        if len(current) == length:
            if is_palindrome(current):
                palindromes.add(current)
            return
        for letter in letters:
            generate_palindromes(letters, current + letter, length)
    generate_palindromes(letters)
    return palindromes