import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[15:90]
    cleaned = re.sub('[^a-zA-Z]', '', substring)
    for length in range(40, 73):
        for i in range(len(cleaned) - length + 1):
            candidate = cleaned[i:i + length].lower()
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result