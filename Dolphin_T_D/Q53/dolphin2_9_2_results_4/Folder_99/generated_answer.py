import re

def palindrome_of_length_at_least_n(input_str):
    palindromes = set()
    input_str = re.sub('[^a-zA-Z]', '', input_str)
    input_str = input_str.lower()
    for i in range(len(input_str)):
        for j in range(i + 115, len(input_str) + 1):
            substr = input_str[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes