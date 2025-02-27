import re

def palindrome_of_length_n(s):
    s = re.sub('\\W+', '', s).lower()
    n = 41
    result = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1]:
            result.add(s[i:i + n])
    return result