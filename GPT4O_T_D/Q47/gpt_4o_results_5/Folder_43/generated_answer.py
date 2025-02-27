import re

def palindromes_of_specific_lengths(s):
    s = s[41:90]
    results = set()
    s = re.sub('[^a-zA-Z]', '', s).lower()
    for length in range(23, 39):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                results.add(substring)
    return results