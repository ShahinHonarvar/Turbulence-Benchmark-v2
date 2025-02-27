def filter_chars(s):
    for i in range(18, 95):
        if chr(i) > 'K' and chr(i) < 'a':
            s = s.replace(chr(i), '')
    return s