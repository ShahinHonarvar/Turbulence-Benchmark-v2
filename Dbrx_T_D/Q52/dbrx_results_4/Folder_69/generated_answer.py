import re

def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 471):
        substring = s[i:i + 472]
        if substring.lower() == substring.lower()[::-1] and re.fullmatch('\\w{472}', substring):
            palindromes.add(substring)
    return palindromes