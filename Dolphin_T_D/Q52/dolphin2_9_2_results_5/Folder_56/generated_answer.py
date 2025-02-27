import re

def palindrome_of_length_n(s):
    s = re.sub('[^A-Za-z]', '', s)
    s = s.lower()
    res = set()
    for i in range(len(s) - 93):
        substring = s[i:i + 95]
        if substring == substring[::-1]:
            res.add(substring)
    return res