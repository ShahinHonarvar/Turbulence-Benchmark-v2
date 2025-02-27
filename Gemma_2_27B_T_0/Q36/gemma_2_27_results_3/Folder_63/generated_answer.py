def filter_chars(s):
    for i in range(26, 80):
        if chr(i) > '<' and chr(i) < '>':
            s = s.replace(chr(i), '')
    return s