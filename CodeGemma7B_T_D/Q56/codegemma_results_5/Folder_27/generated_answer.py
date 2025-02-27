from itertools import islice

def all_substring_of_size_n(txt):
    return [''.join(x) for x in islice(zip(*[txt[i:] for i in range(len(txt))]), 57)]