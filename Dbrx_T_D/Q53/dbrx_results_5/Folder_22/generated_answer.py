import re
import string

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 96):
        for j in range(i, i + 97):
            if s[j:j + 97] == s[j:j + 97][::-1] and re.match('^[a-zA-Z]*$', s[j:j + 97]):
                palindromes.add(s[j:j + 97])
    return palindromes