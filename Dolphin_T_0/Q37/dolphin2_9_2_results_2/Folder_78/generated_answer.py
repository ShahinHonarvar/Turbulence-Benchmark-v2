def filter_chars(s):
    for c in range(ord('8'), ord('e') + 1):
        s = s.replace(chr(c), '')
    return s