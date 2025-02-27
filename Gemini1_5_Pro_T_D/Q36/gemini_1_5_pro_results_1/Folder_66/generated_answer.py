def filter_chars(s):
    for i in range(39, 87):
        if i >= ord('!') and i <= ord('}'):
            c = chr(i)
            s = s.replace(c, '')
    return s