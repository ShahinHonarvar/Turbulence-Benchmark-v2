import re

def palindromes_of_specific_lengths(s):
    substr = s[1:8]
    substr = re.sub('[^a-zA-Z]', '', substr).lower()
    result = set()
    for i in range(len(substr)):
        for length in [3, 4]:
            if i + length <= len(substr):
                candidate = substr[i:i + length]
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result