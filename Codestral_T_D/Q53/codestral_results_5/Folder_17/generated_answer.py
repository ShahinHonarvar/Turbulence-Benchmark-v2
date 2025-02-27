import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    words = re.findall('\\\\b\\\\w+\\\\b', s)
    for word in words:
        if len(word) >= 36 and word == word[::-1]:
            palindromes.add(word)
    return palindromes