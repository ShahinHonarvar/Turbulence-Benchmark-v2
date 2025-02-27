import re

def palindrome_of_length_n(s):
    s = s.lower()
    pattern = '[a-z]{74}'
    palindromes = set()
    for match in re.finditer(pattern, s):
        start, end = (match.start(), match.end())
        substr = s[start:end]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes