import re

def palindrome_of_length_n(string):
    length = 80
    palindromes = set()
    regex = re.compile('[a-zA-Z]{' + str(length) + '}')
    for match in regex.finditer(string):
        substring = match.group(0)
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes