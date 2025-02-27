import re

def palindrome_of_length_n(string):
    string = re.sub('[^A-Za-z]', '', string)
    palindromes = set()
    string = string.lower()
    n = 96
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes