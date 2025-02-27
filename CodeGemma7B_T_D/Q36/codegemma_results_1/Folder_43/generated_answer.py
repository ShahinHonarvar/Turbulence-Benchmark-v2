def filter_chars(s):
    return ''.join([x for x in s if ord(x) not in range(ord('A') + 27, ord('i'))])