import re

def palindrome_of_length_n(s):
    s = re.sub('\\W+', '', s.lower())
    palindromes = set()
    for i in range(len(s) - 100 + 1):
        substr = s[i:i + 100]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes