from itertools import islice

def all_substring_of_size_n(s):
    for i in range(len(s) - 46):
        for a in islice(s[i:], 47):
            yield (''.join(a) if len(set(a)) == 47 else None)