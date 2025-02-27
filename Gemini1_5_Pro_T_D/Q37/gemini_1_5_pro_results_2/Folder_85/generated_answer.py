def filter_chars(s):
    for i in range(28, 66):
        if i >= ord('O') and i <= ord('d'):
            c = chr(i)
            s = s.replace(c, '')
    return s