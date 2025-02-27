def filter_chars(s):
    for c in range(ord('W'), ord('x') + 1):
        s = s.replace(chr(c), '')
    return s