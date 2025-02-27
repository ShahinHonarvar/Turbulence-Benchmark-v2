import re

def palindrome_of_length_n(s):
    s = re.sub('\\W+', '', s)
    s = s.lower()
    n = 53
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes