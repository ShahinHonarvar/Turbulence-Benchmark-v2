import re

def palindrome_of_length_at_least_n(s):
    p = set()
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 77, len(s) + 1):
            ss = s[i:j]
            if ss == ss[::-1]:
                p.add(ss)
    return p