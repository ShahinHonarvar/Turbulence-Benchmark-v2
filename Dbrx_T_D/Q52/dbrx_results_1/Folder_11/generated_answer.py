import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s.lower())
    n = 77
    if n > len(s) or n < 0:
        return set()
    result = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1] and s[i:i + n].isalpha():
            result.add(s[i:i + n])
    return result