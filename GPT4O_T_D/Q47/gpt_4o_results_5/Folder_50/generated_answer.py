import re

def palindromes_of_specific_lengths(s):
    s = s[36:93].lower()
    s = re.sub('[^a-z]', '', s)
    result = set()
    for length in range(10, 36):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result