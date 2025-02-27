import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]+', '', s)
    result = set()
    for i in range(len(s)):
        if s[i].lower() == s[-(i + 1)].lower():
            for j in range(i + 2, len(s) + 1):
                if s[i:j].lower() == s[i:j][::-1].lower() and len(s[i:j]) >= 119:
                    result.add(s[i:j])
    return result