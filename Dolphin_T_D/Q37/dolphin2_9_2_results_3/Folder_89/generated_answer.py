def filter_chars(s):
    for i in range(11, 33):
        if i >= ord('!') and i <= ord('@'):
            s = s.replace(chr(i), '')
    return s