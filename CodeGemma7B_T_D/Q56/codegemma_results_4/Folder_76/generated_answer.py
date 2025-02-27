from itertools import islice

def all_substring_of_size_n(s):
    return list(set((''.join(x) for x in islice(zip(*[s[i:] for i in range(149)]), 149))))