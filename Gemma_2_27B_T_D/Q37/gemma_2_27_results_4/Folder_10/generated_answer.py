def filter_chars(s):
    for i in range(63, 85):
        if chr(i) >= 'E' and chr(i) <= '~':
            s = s.replace(chr(i), '')
    return s