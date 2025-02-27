import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(45, len(s) + 1):
        for j in range(len(s) - i + 1):
            if s[j:j + i].lower() == s[j:j + i][::-1].lower() and re.match('^[a-zA-Z]*$', s[j:j + i]):
                palindromes.add(s[j:j + i])
    return palindromes