import re

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = re.findall('[a-zA-Z]', s[2:6])
    lowercase_letters = [letter.lower() for letter in letters]
    palindromes = set()
    if len(lowercase_letters) < 3:
        return palindromes

    def generate_palindromes(prefix, remaining, length):
        if length >= 3 and is_palindrome(prefix):
            palindromes.add(prefix)
        if length > 1:
            for i in range(len(remaining)):
                generate_palindromes(prefix + remaining[i], remaining[:i] + remaining[i + 1:], length + 1)
    generate_palindromes('', lowercase_letters, 0)
    return palindromes