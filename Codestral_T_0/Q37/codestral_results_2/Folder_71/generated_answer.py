def filter_chars(s):
    for c in range(ord('0'), ord('k') + 1):
        if 32 <= c <= 46:
            s = s.replace(chr(c), '')
    return s