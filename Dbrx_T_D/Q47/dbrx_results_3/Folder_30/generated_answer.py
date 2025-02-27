import re
import string

def palindromes_of_specific_lengths(input_string):
    english_letters = set(string.ascii_letters)
    palindromes = set()
    for length in range(55, 72):
        for index in range(14, len(input_string) - length + 2):
            substring = input_string[index:index + length]
            if len(set(substring) - english_letters) == 0 and substring.upper() == substring:
                palindromes.add(substring)
    return palindromes