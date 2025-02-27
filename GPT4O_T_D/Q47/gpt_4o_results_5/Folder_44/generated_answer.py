import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = re.sub('[^a-z]', '', s[18:99])
    results = set()
    for length in range(31, 52):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                results.add(substring)
    return results