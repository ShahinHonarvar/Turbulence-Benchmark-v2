import re

def palindrome_of_length_n(s):
    pattern = '[A-Za-z]{10}'
    palindromes = set()
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if re.match(pattern, substring):
            palindromes.add(substring)
    return palindromes