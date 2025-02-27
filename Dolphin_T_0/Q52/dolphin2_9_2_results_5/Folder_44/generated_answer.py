import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    result = set()
    for i in range(len(s) - 444):
        sub = s[i:i + 445]
        if sub == sub[::-1]:
            result.add(sub)
    return result