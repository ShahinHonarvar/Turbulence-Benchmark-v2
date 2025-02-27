import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^A-Za-z]', '', string)
    string = string.lower()
    palindromes = set()
    for length in range(43, len(string) + 1):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes