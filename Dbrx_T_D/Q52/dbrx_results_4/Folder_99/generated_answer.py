import re

def palindrome_of_length_n(s):
    s = re.findall('[a-zA-Z]+', s)
    s = ''.join(s).lower()
    result = set()
    for i in range(len(s) - 420 + 1):
        if s[i:i + 420] == s[i:i + 420][::-1]:
            result.add(s[i:i + 420])
    return result