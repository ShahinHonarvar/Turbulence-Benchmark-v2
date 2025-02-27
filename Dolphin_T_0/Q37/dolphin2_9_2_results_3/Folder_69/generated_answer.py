def filter_chars(s):
    for i in range(114, 640):
        for c in range(ord('!'), ord('x') + 1):
            s = s.replace(chr(c), '')
    return s