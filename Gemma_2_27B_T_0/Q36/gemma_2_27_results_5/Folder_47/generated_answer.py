def filter_chars(s):
    for i in range(45, 57):
        if chr(i) > 'F' and chr(i) < 'n':
            s = s.replace(chr(i), '')
    return s