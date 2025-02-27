import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for length in range(25, len(s) + 1):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if re.sub('[^a-z]', '', substring) == re.sub('[^a-z]', '', substring[::-1]):
                result.add(re.sub('[^a-z]', '', substring))
    return result