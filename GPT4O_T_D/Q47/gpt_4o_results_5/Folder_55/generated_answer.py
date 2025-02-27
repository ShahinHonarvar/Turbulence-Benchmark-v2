import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[10:76]
    substring = re.sub('[^a-z]', '', substring)
    palindromes = set()
    for length in range(10, 21):
        for start in range(len(substring) - length + 1):
            segment = substring[start:start + length]
            if segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes