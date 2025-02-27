import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for m in re.finditer('\\\\b\\\\w+\\\\b', s):
        word = m.group()
        if len(word) >= 122 and word == word[::-1]:
            palindromes.add(word)
    return palindromes