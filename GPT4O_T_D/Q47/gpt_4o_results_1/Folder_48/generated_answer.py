import re

def palindromes_of_specific_lengths(s):
    s = s[155:284]
    result = set()
    for length in range(104, 121):
        for i in range(len(s) - length + 1):
            candidate = s[i:i + length]
            cleaned_candidate = re.sub('[^a-zA-Z]', '', candidate).lower()
            if cleaned_candidate == cleaned_candidate[::-1]:
                result.add(candidate)
    return result