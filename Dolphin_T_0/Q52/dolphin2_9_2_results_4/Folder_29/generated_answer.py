import re

def palindrome_of_length_n(string):
    string = re.sub('[^A-Za-z]', '', string)
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 18):
        pal = string[i:i + 19]
        if pal == pal[::-1]:
            palindromes.add(pal)
    return palindromes