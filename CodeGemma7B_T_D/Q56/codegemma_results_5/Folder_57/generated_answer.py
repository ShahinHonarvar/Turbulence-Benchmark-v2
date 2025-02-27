from itertools import combinations_with_replacement

def all_substring_of_size_n(text):
    if len(text) < 60:
        return []
    res = set()
    for i in range(len(text) - 59):
        substring = text[i:i + 60]
        if len(substring) == len(set(substring)):
            res.add(substring)
    return list(res)