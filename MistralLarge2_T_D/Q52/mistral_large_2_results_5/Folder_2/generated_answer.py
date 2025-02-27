import re

def palindrome_of_length_n(s):
    n = 147
    result = set()
    s = re.sub('[^A-Za-z]', '', s).lower()
    length = len(s)
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            result.add(substr)
    return result