import sys

def return_n_smallest_chars(string):
    chars = sorted(list(set(string)), key=sys.getsizeof)
    return chars[:2]