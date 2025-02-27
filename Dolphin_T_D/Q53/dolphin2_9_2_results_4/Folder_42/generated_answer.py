import re

def palindrome_of_length_at_least_n(s):
    result = set()
    for word in re.findall('\\b\\w+\\b', s.lower()):
        if len(word) >= 44:
            result.add(word)
    return result