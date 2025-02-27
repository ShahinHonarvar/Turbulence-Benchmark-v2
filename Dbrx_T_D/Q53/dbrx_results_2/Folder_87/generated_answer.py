import re

def palindrome_of_length_at_least_n(s):
    words = re.findall('\\b\\w\\w+\\b', s.lower())
    palindromes = set()
    for word in words:
        if len(word) >= 18 and word == word[::-1]:
            palindromes.add(word)
    return palindromes