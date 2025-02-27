import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[26:91]
    cleaned_substring = re.sub('[^a-zA-Z]', '', substring)
    for length in range(27, 59):
        for i in range(0, len(cleaned_substring) - length + 1):
            candidate = cleaned_substring[i:i + length]
            if candidate.lower() == candidate[::-1].lower():
                result.add(candidate)
    return result