def filter_chars(s):
    for c in range(ord('m'), ord('w') + 1):
        s = s.replace(chr(c), '')
    return s