def filter_chars(s):
    for i in range(73, 75):
        for c in range(ord('U'), ord('l') + 1):
            if chr(c) in s:
                s = s.replace(chr(c), '')
    return s