from itertools import islice

def return_nth_smallest_ascii(s):
    return min(islice(sorted(s[0:7]), 6, None))