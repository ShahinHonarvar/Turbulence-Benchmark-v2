import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    strings = re.findall('[a-zA-Z]{149,}', s)
    palindromes = set()
    for string in strings:
        if string == string[::-1]:
            palindromes.add(string)
    return palindromes