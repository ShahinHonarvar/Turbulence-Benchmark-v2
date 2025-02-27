import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 58):
        for j in range(i + 29, i + 58 - 29 * (i > len(s) - 58)):
            if s[i:j] == s[i:j][::-1] and re.match('^[a-zA-Z]*$', s[i:j]):
                palindromes.add(s[i:j])
    return palindromes