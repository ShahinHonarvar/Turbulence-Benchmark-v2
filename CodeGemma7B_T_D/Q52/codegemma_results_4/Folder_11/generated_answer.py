import re

def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 76, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result