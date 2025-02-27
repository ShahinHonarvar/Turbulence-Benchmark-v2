import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    n = 51
    palindromes = {string[i:i + n] for i in range(len(string)) if string[i:i + n] == string[i:i + n][::-1]}
    return palindromes