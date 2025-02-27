def filter_chars(s):
    for i in range(71, 97):
        c = chr(i)
        if c >= '_' and c <= 'o':
            s = s.replace(c, '')
    return s