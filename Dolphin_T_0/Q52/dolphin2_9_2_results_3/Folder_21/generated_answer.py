import re

def palindrome_of_length_n(input_str):
    input_str = re.sub('[^a-zA-Z]', '', input_str)
    input_str = input_str.lower()
    length = 407
    palindromes = set()
    for i in range(len(input_str) - length + 1):
        substring = input_str[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes