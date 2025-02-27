import re

def palindrome_of_length_n(s):
    s = re.sub('\\W+', '', s.lower())
    palindromes = set()
    for i in range(len(s) - 45):
        substring = s[i:i + 46]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes