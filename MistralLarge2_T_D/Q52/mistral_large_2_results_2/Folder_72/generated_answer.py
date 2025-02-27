import re

def palindrome_of_length_n(string):
    length = 16
    palindromes = set()
    string = re.sub('[^a-zA-Z]', '', string).lower()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes