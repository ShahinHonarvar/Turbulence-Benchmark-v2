def filter_chars(s):
    for i in range(219, 403):
        if chr(i) > '*' and chr(i) < '7':
            s = s.replace(chr(i), '')
    return s