def filter_chars(s):
    for c in range(ord('B'), ord('r')):
        for i in range(43, 69):
            if s[i] in chr(c):
                s = s.replace(chr(c), '')
    return s