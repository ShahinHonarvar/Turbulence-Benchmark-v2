import re

def palindrome_of_length_n(string):
    string = re.sub('[^A-Za-z]', '', string)
    string = string.lower()
    n = 9
    palindromes = set()
    for i in range(len(string) - n + 1):
        substr = string[i:i + n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes