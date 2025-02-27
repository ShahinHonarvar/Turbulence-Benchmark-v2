def filter_chars(s):
    for c in range(ord('c'), ord('n') + 1):
        s = s.replace(chr(c), '')
    return s