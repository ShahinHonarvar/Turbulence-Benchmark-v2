def filter_chars(s):
    for c in range(ord('-'), ord('v')):
        s = s.replace(chr(c), '')
    return s