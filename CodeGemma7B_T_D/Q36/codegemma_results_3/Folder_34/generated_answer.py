from itertools import dropwhile

def filter_chars(s):
    return ''.join(dropwhile(lambda c: c <= '?' or c >= 'm', s[10:79]))