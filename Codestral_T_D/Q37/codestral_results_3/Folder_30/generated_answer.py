def filter_chars(s):
    for c in range(ord('K'), ord(']') + 1):
        s = s.replace(chr(c), '')
    return s