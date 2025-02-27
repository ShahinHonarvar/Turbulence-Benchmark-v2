import re

def palindromes_of_specific_lengths(s):
    s = s[:51].lower()
    matches = re.findall('\\\\b[a-z]{50,100}\\\\b', s)
    palindromes = {word for word in matches if word == word[::-1]}
    return palindromes