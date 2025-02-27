def filter_chars(s):
    for i in range(58, 81):
        if i >= ord('5') and i <= ord('>'):
            c = chr(i)
            s = s.replace(c, '')
    return s