import re

def palindrome_of_length_at_least_n(string):
    n = 59
    lowered_string = string.lower()
    pattern = '[a-z]{' + str(n) + ',}'
    matches = re.findall(pattern, lowered_string)
    palindromes = {word for word in matches if word == word[::-1]}
    return palindromes