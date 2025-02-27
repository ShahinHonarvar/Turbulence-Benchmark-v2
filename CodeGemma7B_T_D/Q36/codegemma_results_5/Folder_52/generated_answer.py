from itertools import groupby

def filter_chars(str):
    return ''.join((k for k, g in groupby(str) if ord(k) not in range(49, 57) or ord(k) > ord('i') or ord(k) < ord('a')))