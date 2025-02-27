import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j + 1]
            if substr == substr[::-1] and re.match('^[a-zA-Z]*$', substr):
                if len(substr) >= 10:
                    palindromes.add(substr.lower())
    return palindromes