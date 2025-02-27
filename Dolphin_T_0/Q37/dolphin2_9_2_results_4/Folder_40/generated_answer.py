def filter_chars(s):
    for c in range(ord('*'), ord('s') + 1):
        s = s.replace(chr(c), '')
    return s