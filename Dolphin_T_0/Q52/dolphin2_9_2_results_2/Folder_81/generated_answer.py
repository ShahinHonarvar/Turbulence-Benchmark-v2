import re

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s)
    result = set()
    for i in range(len(s) - 98):
        candidate = s[i:i + 99]
        if ''.join(reversed(candidate)).lower() == candidate.lower():
            result.add(candidate)
    return result