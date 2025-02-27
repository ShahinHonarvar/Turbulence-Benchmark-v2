import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s.lower())
    result = set()
    if len(s) < 42:
        return result
    for i in range(len(s) - 42 + 1):
        if s[i:i + 42] == s[i:i + 42][::-1]:
            result.add(s[i:i + 42])
    return result