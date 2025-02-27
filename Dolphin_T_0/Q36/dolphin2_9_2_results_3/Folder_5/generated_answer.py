def filter_chars(s):
    for char in range(55, 66):
        c = chr(char)
        while c in s:
            s = s.replace(c, '', 1) if c > 'f' and c < '|' else s
    return s