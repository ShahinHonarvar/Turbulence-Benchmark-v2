import itertools

def all_substring_of_size_n(s):
    if not s:
        return []
    bcl = set(s)
    ss = []
    for p in itertools.permutations(''):
        ss += [p]
    return sorted(set(ss))