import re

def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 278):
        substring = s[i:i + 279].lower()
        if re.match('^[a-z]*$', substring) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes