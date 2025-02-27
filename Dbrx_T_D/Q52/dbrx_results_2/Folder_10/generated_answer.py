import re

def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 53):
        substring = s[i:i + 54].lower()
        if bool(re.match('^[a-z]{54}$', substring)) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes