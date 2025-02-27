import re

def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    palindromes = set()
    strings_length = len(input_string)
    for i in range(strings_length):
        for j in range(i + 41, strings_length + 1):
            element = input_string[i:j]
            if element == element[::-1]:
                palindromes.add(element)
    return palindromes