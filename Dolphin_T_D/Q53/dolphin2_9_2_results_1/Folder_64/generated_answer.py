import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    for i in range(len(string) - 8):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes