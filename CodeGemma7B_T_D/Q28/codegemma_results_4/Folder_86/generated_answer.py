from functools import partial
from itertools import islice

def return_nth_smallest_ascii(in_str):
    return next(islice(sorted([char for char in in_str[44:70]], key=ord), 14, 15))