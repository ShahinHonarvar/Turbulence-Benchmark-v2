import re

def palindrome_of_length_n(s):
    s = re.sub('[^A-Za-z]', '', s)
    s = s.lower()
    result = set()
    for i in range(len(s) - 34):
        sub = s[i:i + 35]
        if sub == sub[::-1]:
            result.add(sub)
    return result