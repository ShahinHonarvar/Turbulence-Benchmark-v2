def filter_chars(string):
    return ''.join([c for c in string if not (29 <= ord(c) <= 79 and ord(c) >= ord('K') and (ord(c) <= ord('z')))])