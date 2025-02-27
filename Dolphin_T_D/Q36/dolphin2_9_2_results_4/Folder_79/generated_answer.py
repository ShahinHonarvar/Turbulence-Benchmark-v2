def filter_chars(s):
    for c in range(ord('!'), ord('A')):
        ch = chr(c)
        s = s.replace(ch, '')
    return s