import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 27 + 1):
        current_substr = s[i:i + 27]
        current_substr = ''.join((c.lower() for c in current_substr if c.isalpha()))
        if current_substr and current_substr == current_substr[::-1]:
            palindromes.add(current_substr)
    return palindromes