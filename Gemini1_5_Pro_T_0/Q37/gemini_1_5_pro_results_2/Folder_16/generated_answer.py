def filter_chars(s):
    for i in range(225, 382):
        if chr(i) >= 'D' and chr(i) <= 'Y':
            s = s.replace(chr(i), '')
    return s