import re

def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    for length in range(23, len(input_string) + 1):
        for i in range(len(input_string) - length + 1):
            substring = input_string[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes