import re

def palindrome_of_length_n(s):
    s = re.sub('\\W+', '', s)
    result = set()
    for i in range(len(s) - 61):
        if s[i:i + 63].lower() == s[i:i + 63].lower()[::-1]:
            result.add(s[i:i + 63])
    return result