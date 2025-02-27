import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for match in re.finditer('\\\\b[a-z]{34,}\\\\b', s):
        word = match.group()
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes