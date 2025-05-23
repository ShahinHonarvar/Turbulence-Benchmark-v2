import re

def palindrome_of_length_n(string):
    string = re.sub('\\\\W+', '', string.lower())
    palindromes = set()
    length = 83
    if length <= len(string):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes