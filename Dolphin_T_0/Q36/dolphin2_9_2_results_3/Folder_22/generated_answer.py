def filter_chars(s):
    for c in range(ord(';') + 1, ord('z')):
        s = s.replace(chr(c), '')
    return s