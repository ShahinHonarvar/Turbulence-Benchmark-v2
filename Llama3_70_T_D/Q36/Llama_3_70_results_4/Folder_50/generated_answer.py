def filter_chars(s):
    for i in range(61, 88):
        c = chr(i)
        if '%' < c < 'q' and c in s:
            s = s.replace(c, '')
    return s