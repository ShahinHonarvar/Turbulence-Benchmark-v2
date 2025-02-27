def filter_chars(s):
    for i in range(672, 709):
        c = s[i]
        if c > 'X' and c < '}':
            s = s.replace(c, '')
    return s