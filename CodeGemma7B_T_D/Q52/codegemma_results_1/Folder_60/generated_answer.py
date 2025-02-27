import re

def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 88 + 1):
        substring = s[i:i + 88]
        if re.fullmatch('[a-zA-Z]{88}', substring):
            palindromes.add(substring)
    return palindromes