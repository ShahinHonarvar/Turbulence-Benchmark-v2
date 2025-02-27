from functools import reduce

def all_substring_of_size_n(s):
    if len(s) < 68:
        return []
    substrs = [s[i:j] for i in range(len(s)) for j in range(i + 1, min(i + 68 + 1, len(s) + 1))]
    return [substr for substr in set(substrs) if len(substr) == 68 and reduce(lambda x, y: x and substr.count(y) == 1, substr, True)]