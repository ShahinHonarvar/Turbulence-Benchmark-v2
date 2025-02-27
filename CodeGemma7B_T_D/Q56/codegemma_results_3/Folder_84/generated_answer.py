from itertools import product

def all_substring_of_size_n(text):
    max_size_n = 114
    result = set()
    if len(text) < max_size_n:
        return list(result)
    char_set = set(text)
    for i in range(len(text)):
        for end in range(i + max_size_n):
            substring = text[i:end]
            if len(substring) == max_size_n and len(set(substring)) == max_size_n:
                result.add(substring)
    return list(result)