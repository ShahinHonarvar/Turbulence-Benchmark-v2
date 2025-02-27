def filter_chars(s):
    for c in s:
        if c >= 'B' and c <= 'H' and (c in s[7:8]):
            s = s.replace(c, '')
    return s