import re

def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    cleaned_input = re.sub('\\W+', '', input_string.lower())
    for length in range(10, len(cleaned_input) + 1):
        for i in range(len(cleaned_input) - length + 1):
            substring = cleaned_input[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes