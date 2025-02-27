import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s.lower())
    n = 7
    return {s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1) if s[i:j] == s[i:j][::-1]}