import re

def palindrome_of_length_n(txt):
    L = len(txt)
    str_lower = re.sub('[^a-z]', '', txt.lower())
    res = set()
    for i in range(L - 44):
        for j in range(i + 1, L - 43):
            if palindrome(str_lower[i:j + 1]):
                res.add(txt[i:j + 1])
    return res

def palindrome(s):
    return s == s[::-1]