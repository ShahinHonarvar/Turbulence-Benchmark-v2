def filter_chars(s):
    for i in range(41, 56):
        if i > ord('Z') and i < ord('c'):
            c = chr(i)
            s = s.replace(c, '')
    return s