import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    substrings = re.findall(f'(?=([a-zA-Z]{{464}}))', string)
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes