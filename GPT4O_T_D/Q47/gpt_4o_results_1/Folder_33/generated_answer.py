import re

def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    s_sub = s[130:296]
    s_sub = re.sub('[^a-z]', '', s_sub)
    for length in range(103, 159):
        for i in range(len(s_sub) - length + 1):
            substring = s_sub[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result