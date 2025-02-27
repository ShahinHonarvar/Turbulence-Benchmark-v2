import re

def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    for i in range(24, len(input_string) + 1):
        for j in range(len(input_string) - i + 1):
            substring = input_string[j:j + i]
            if substring == substring[::-1] and all((char.isalpha() for char in substring)):
                palindromes.add(substring)
    return palindromes