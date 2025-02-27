def filter_chars(s):
    for i in range(18, 64):
        if i >= ord('3') and i <= ord('B'):
            c = chr(i)
            s = s.replace(c, '')
    return s