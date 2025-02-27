import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(147, len(s) + 1):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i].lower()
            if substring == substring[::-1] and bool(re.search('\\b\\w*{}\\w*\\b', substring)):
                palindromes.add(substring)
    return palindromes