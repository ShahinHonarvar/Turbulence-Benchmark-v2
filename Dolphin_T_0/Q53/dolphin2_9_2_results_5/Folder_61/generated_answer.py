import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for word in re.findall('\\\\b\\\\w+\\\\b', s.lower()):
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)
    return palindromes