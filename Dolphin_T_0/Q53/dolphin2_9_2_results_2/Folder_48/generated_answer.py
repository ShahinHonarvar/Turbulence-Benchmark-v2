import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^A-Za-z]', '', s)
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 149, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                res.add(substr)
    return res