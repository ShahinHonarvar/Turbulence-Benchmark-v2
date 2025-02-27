import re

def palindrome_of_length_n(s):
    result = set()
    n = 67
    for i in range(len(s) - n + 1):
        pal = s[i:i + n]
        if pal.lower() == pal.lower()[::-1] and re.fullmatch('\\w*', pal):
            result.add(pal)
    return result