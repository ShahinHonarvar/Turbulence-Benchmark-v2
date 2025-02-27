def filter_chars(s):
    for c in range(ord('W') + 1, ord('x')):
        s = s.replace(chr(c), '')
    return s