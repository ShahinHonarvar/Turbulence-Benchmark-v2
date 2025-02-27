def filter_chars(s):
    for c in range(ord('0'), ord('9') + 1):
        s = s.replace(chr(c), '')
    for c in range(ord('A'), ord('K') + 1):
        s = s.replace(chr(c), '')
    return s