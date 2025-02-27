import re

def palindromes_of_specific_lengths(s):
    result = set()
    s = re.sub('[^a-zA-Z]', '', s[33:86]).lower()
    for length in range(26, 32):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if sub == sub[::-1]:
                result.add(sub)
    return result