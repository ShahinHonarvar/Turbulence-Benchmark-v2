import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s.lower())
    n = 186
    if n > len(s):
        return set()
    return {s[i:n + i] for i in range(len(s)) if s[i:n + i] == s[i:n + i][::-1]}