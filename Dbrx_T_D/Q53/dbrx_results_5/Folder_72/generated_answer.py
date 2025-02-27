import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 88 + 1):
        for j in range(88):
            if s[i:i + j + 1] == s[i:i + j + 1][::-1] and re.fullmatch('[a-zA-Z]*', s[i:i + j + 1]):
                palindromes.add(s[i:i + j + 1])
    return {palindrome for palindrome in palindromes if len(palindrome) >= 88}