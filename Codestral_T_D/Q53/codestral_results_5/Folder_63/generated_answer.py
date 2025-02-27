import re

def palindrome_of_length_at_least_n(s):
    words = re.findall('\\\\b[a-zA-Z]+\\\\b', s.lower())
    palindromes = set()
    for word in words:
        if len(word) >= 37 and word == word[::-1]:
            palindromes.add(word)
    return palindromes