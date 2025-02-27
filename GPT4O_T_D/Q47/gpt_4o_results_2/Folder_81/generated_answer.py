import re

def palindromes_of_specific_lengths(s):
    s = s[12:123].lower()
    s = re.sub('[^a-z]', '', s)
    results = set()
    for length in range(12, 221):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr == substr[::-1]:
                results.add(substr)
    return results