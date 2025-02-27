import re

def palindromes_of_specific_lengths(s):
    s = s[10:60]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    result = set()
    for length in range(18, 37):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result