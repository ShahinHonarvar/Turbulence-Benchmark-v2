def filter_chars(string):
    return ''.join((c for c in string if not (35 <= ord(c) <= 89 and ord(c) >= ord('E') and (ord(c) <= ord('t')))))