import re

def palindrome_of_length_n(s):
    s = re.sub('\\W+', '', s).lower()
    result = set()
    for i in range(len(s) - 91):
        substring = s[i:i + 92]
        if substring == substring[::-1]:
            result.add(substring)
    return result