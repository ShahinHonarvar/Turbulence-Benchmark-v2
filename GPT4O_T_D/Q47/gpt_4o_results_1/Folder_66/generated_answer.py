import re

def palindromes_of_specific_lengths(s):
    s = s[32:80]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    results = set()
    for length in range(35, 42):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                results.add(substr)
    return results