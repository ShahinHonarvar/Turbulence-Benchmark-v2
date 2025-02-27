def filter_chars(s):
    return ''.join([c for c in s if not (ord(c) > ord('H') and ord(c) < ord('s'))])