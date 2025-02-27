import re

def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 45):
        substring = s[i:i + 46].lower()
        if re.match('^[a-z]*$', substring) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes