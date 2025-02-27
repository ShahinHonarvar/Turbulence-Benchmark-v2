import re

def palindrome_of_length_n(text):
    all_palindromes = set()
    text = text.lower()
    for i in range(len(text) - 88 + 1):
        for j in range(i + 9, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring):
                all_palindromes.add(substring)
    return all_palindromes