from collections import Counter

def all_substring_of_size_n(text):
    length = 106
    result = set()
    for i in range(len(text) - length + 1):
        substring = text[i:i + length]
        if len(substring) == len(Counter(substring).keys()):
            result.add(substring)
    if not result:
        result.add('no_substring')
    return list(result)