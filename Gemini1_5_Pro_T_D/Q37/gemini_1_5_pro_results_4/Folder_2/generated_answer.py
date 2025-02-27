def filter_chars(s):
    new_s = ''
    for i, c in enumerate(s):
        if 477 <= i <= 984 and ',' <= c <= 'V':
            s = s.replace(c, '')
    return s