import re

def palindrome_of_length_n(s):
    s = re.sub('[A-Z]', lambda x: x.group().lower(), s)
    palindromes = set()
    length = 96
    for i in range(len(s) - length + 1):
        if s[i:i + length] == s[i:i + length][::-1]:
            palindromes.add(s[i:i + length])
    return palindromes