import re

def palindrome_of_length_at_least_n(string, n=44):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    palindromes = {string[i:j] for i in range(len(string)) for j in range(i + n, len(string) + 1) if string[i:j] == string[i:j][::-1]}
    return palindromes