import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[24:98]
    substring = re.sub('[^a-zA-Z]', '', substring)
    normalized = substring.lower()
    for length in range(10, 37):
        for start in range(len(normalized) - length + 1):
            segment = normalized[start:start + length]
            if segment == segment[::-1]:
                result.add(segment)
    return result