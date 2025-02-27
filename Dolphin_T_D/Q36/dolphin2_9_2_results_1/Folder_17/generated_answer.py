def filter_chars(s):
    for c in range(ord('a'), ord('z') + 1):
        if c > ord('K') and c < ord('a'):
            s = s.replace(chr(c), '')
    return s