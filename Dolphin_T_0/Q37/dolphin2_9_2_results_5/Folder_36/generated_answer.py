def filter_chars(s):
    for c in s:
        if 259 <= s.index(c) <= 502 and ',' <= c <= '3':
            s = s.replace(c, '')
    return s