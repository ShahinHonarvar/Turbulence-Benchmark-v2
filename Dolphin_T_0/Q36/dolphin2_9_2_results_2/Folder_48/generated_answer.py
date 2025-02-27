def filter_chars(s):
    for c in range(ord('A'), ord('f') + 1):
        s = s.replace(chr(c), '')
    return s