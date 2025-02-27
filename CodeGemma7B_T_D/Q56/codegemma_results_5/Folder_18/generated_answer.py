from itertools import islice
from functools import partial
from collections import defaultdict

def all_substring_of_size_n(string):
    res = []
    for idx in range(len(string)):
        chars = defaultdict(int)
        for jdx in range(idx, min(idx + 63, len(string))):
            chars[string[jdx]] += 1
            if len(chars) == 63 and max(chars.values()) == 1:
                res.append(string[idx:jdx + 1])
    return res