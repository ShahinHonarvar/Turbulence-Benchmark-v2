import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    n = 56
    result = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if sub == sub[::-1]:
            result.add(sub.lower())
    return result