import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    words = re.findall('\\\\b\\\\w+\\\\b', s)
    palindromes = {word for word in words if word == word[::-1] and len(word) >= 7 and word.isalpha()}
    return palindromes