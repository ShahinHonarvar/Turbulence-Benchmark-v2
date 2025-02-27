def filter_chars(s):
    for i in range(86, 93):
        if i >= ord('!') and i <= ord('s'):
            s = s.replace(chr(i), '')
    return s