def filter_chars(v):
    return ''.join([x for x in v if ord(x) not in range(ord('&'), ord('c')) or ord(x) > ord('g')])