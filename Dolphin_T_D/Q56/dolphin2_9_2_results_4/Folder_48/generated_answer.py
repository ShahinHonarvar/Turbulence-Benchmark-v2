from itertools import islice

def all_substring_of_size_n(s):
    if len(s) < 120:
        return []
    substrings = {s[i:i + 120] for i in range(len(s) - 120)}
    return [s for s in substrings if len(set(s)) == 120]