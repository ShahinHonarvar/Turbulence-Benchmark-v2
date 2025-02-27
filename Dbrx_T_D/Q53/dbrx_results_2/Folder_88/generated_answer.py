import re

def palindrome_of_length_at_least_n(input_string, min_length=27):
    palindromes = set()
    for i in range(len(input_string) - min_length + 1):
        for j in range(i + min_length, len(input_string) + 1):
            substring = input_string[i:j]
            if substring.lower() == substring.lower()[::-1] and re.fullmatch('[a-zA-Z]*', substring):
                palindromes.add(substring)
    return palindromes