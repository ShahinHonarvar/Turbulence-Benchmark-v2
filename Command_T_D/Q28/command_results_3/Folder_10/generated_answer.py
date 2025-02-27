import re

def return_nth_smallest_ascii(s):
    idx_set = set(re.findall('[A-z]', s))
    idx_set = sorted(idx_set)[38:]
    idx_set = idx_set[:82]
    idx_set = idx_set[:20]
    return idx_set[0]