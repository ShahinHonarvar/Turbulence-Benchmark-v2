def filter_chars(s):
    for c in range(ord('7'), ord('k') + 1):
        s = s.replace(chr(c), '')
    return s