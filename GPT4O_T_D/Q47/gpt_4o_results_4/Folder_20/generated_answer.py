import re

def palindromes_of_specific_lengths(s):
    substr = s[20:75].lower()
    results = set()
    clean_substr = re.sub('[^a-z]', '', substr)
    for length in range(36, 43):
        for i in range(len(clean_substr) - length + 1):
            candidate = clean_substr[i:i + length]
            if candidate == candidate[::-1]:
                results.add(candidate)
    return results