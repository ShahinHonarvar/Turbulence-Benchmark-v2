def filter_chars(s):
    for c in range(ord(':'), ord('L') + 1):
        s = s.replace(chr(c), '')
    return s