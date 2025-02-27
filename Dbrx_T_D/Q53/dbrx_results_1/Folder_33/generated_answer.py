import re

def get_english_letters(input_string):
    return ''.join((e.lower() if 'a' <= e <= 'z' else '' for e in input_string))

def is_palindrome(input_string):
    english_letters = get_english_letters(input_string)
    return english_letters == english_letters[::-1]

def palindrome_of_length_at_least_n(input_string, n):
    palindromes = set()
    for i in range(len(input_string) - n + 1):
        for j in range(i, len(input_string) - i + 1):
            if is_palindrome(input_string[i:j + 1]):
                palindromes.add(input_string[i:j + 1])
    return palindromes