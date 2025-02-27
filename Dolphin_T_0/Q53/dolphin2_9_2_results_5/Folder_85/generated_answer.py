import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    words = re.findall('[a-zA-Z]+', s)
    palindromes = set()
    for word in words:
        if len(word) >= 85:
            palindromes.add(word)
    return palindromes