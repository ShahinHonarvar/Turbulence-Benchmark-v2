import re

def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 69 + 1):
        test_string = s[i:i + 69].lower()
        if test_string == test_string[::-1] and re.fullmatch('[a-zA-Z]*', test_string):
            palindromes.add(test_string)
    return palindromes