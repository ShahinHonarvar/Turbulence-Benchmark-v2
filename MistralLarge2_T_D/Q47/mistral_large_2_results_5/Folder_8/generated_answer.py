import re

def palindromes_of_specific_lengths(s):
    sub_string = s[17:73].lower()
    pattern = re.compile('\\\\b[a-z]{50,51}\\\\b')
    words = pattern.findall(sub_string)
    palindromes = {word for word in words if word == word[::-1]}
    return palindromes