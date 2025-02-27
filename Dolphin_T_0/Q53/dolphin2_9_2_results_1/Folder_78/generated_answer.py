import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = re.sub('\\\\W+', '', s).lower()
    for i in range(len(s) - 95):
        substring = s[i:i + 96]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes