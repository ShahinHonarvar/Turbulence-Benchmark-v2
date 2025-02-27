import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 73):
        substring = s[i:i + 74]
        if re.match('^[a-z]*$', substring) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes