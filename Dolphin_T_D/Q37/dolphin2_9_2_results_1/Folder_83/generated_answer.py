def filter_chars(s):
    for c in range(ord('K'), ord('z') + 1):
        s = s.replace(chr(c), '')
    return s