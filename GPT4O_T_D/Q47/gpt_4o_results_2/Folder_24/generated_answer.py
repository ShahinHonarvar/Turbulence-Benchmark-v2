import re

def palindromes_of_specific_lengths(s):
    substr = s[12:93]
    substr = re.sub('[^a-zA-Z]', '', substr)
    substr_lower = substr.lower()
    palindromes = set()
    for start in range(len(substr_lower)):
        for length in range(42, 78):
            if start + length > len(substr_lower):
                break
            part = substr_lower[start:start + length]
            if part == part[::-1]:
                palindromes.add(part)
    return palindromes