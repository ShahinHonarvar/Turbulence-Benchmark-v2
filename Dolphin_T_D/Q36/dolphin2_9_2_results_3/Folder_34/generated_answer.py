def filter_chars(s):
    for c in range(ord('?'), ord('m')):
        s = s.replace(chr(c), '')
    return s