def filter_chars(s):
    for c in range(ord('J'), ord('Q') + 1):
        s = s.replace(chr(c), '')
    return s