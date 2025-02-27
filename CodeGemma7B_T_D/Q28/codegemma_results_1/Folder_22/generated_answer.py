import sys

def return_nth_smallest_ascii(s):
    if len(s) < 17:
        return sys.maxsize
    return sorted(s[0:17])[16]