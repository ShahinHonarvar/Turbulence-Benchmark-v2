import re

def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 55):
        substring = s[i:i + 56]
        if substring.lower() == substring.lower()[::-1] and re.match('^[a-zA-Z]+$', substring):
            palindromes.add(substring)
    return palindromes