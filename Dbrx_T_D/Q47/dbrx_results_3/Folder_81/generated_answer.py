import re

def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(12, 122 + 1):
        for j in range(len(s) - i + 1):
            if re.match('^[a-zA-Z]+$', s[j:j + i]):
                palindrome = s[j:j + i].lower()
                if palindrome == palindrome[::-1]:
                    result.add(palindrome)
    return result