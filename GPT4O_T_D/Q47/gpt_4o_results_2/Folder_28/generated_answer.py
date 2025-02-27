import re

def palindromes_of_specific_lengths(s):
    substring = s[32:72]
    matches = set()
    substring = re.sub('[^a-zA-Z]', '', substring).lower()
    for length in range(21, 33):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1]:
                matches.add(candidate)
    return matches