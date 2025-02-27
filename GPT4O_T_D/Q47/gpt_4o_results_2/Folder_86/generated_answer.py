import re

def palindromes_of_specific_lengths(s):
    substring = s[30:96]
    result = set()
    for length in range(34, 56):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            candidate_alpha = re.sub('[^a-zA-Z]', '', candidate).lower()
            if candidate_alpha == candidate_alpha[::-1]:
                result.add(candidate)
    return result