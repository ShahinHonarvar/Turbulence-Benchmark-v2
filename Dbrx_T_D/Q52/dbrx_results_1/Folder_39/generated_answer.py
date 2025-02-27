import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 58):
        if s[i:i + 59] == s[i:i + 59][::-1] and re.match('^[A-Za-z]*$', s[i:i + 59]):
            palindromes.add(s[i:i + 59])
    return palindromes