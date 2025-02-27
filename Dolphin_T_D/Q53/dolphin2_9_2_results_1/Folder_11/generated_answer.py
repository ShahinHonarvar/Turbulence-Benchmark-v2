import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub('[^A-Za-z]', '', string)
    string = string.lower()
    for i in range(len(string) - 53):
        for j in range(i + 54, len(string) + 1):
            candidate = string[i:j]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes