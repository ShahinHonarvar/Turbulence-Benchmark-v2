import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    length = 94
    result = set()
    for i in range(len(s) - length + 1):
        if s[i:i + length] == s[i:i + length][::-1]:
            result.add(s[i:i + length])
    return result