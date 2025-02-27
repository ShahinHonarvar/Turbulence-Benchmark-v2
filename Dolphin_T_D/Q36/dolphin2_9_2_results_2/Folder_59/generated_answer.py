def filter_chars(s):
    for c in range(ord('?'), ord('k')):
        s = s.replace(chr(c), '')
    return s