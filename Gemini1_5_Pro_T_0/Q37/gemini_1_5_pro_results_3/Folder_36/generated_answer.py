def filter_chars(s):
    for i in range(259, 503):
        c = chr(i)
        if ',' <= c <= '3':
            s = s.replace(c, '')
    return s