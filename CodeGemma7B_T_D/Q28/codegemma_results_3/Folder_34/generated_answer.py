from itertools import islice

def return_nth_smallest_ascii(txt):
    return islice(sorted(txt), 19).next()