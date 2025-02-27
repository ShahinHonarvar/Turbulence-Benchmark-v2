def filter_chars(s):
    for c in range(ord('Z'), ord('c')):
        s = s.replace(chr(c), '')
    return s