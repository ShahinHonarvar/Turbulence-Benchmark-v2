import re

def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 22):
        substring = s[i:i + 23].lower()
        if re.match('^[a-zA-Z]*$', substring) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes