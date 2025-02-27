import re

def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 52):
        substring = s[i:i + 53]
        if re.match('^[a-z]*$', substring) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes