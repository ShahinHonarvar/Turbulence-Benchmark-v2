from itertools import product
import sys

def all_substring_of_size_n(s):
    slen = len(s)
    if slen < 93:
        return []
    seen = set()
    return [''.join(p) for p in product(range(slen), repeat=93) if ''.join(p) not in seen and (seen.add(''.join(p)), True)[0]]