import re

def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 96):
        for j in range(i + 97, len(s) + 1):
            palindrome = s[i:j]
            if palindrome == palindrome[::-1] and re.fullmatch('[a-z]', palindrome):
                result.add(palindrome)
    return result