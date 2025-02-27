def filter_chars(s):
    for c in range(ord('E'), ord('t') + 1):
        for i in range(35, 90):
            s = s.replace(chr(c), '')
    return s