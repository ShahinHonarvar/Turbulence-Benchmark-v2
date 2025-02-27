def filter_chars(s):
    for i in range(4, 5):
        for c in range(ord('7'), ord('o') + 1):
            s = s.replace(chr(c), '')
    return s