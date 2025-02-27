import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[155:284].lower()
    letters_only = re.sub('[^a-z]', '', substring)
    n = len(letters_only)
    for length in range(104, 121):
        for start in range(n - length + 1):
            candidate = letters_only[start:start + length]
            if candidate == candidate[::-1]:
                result.add(letters_only[start:start + length].lower())
    return result