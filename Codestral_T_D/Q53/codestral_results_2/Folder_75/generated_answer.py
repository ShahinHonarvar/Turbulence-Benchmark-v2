import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    words = re.findall('\\\\b[a-z]+\\\\b', s)
    for word in words:
        if len(word) >= 40 and word == word[::-1]:
            palindromes.add(word)
    return palindromes