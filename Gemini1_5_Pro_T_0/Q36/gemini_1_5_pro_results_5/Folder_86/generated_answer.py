def filter_chars(s):
    for i in range(672, 709):
        if i >= len(s):
            break
        c = s[i]
        if c > 'X' and c < '}':
            s = s.replace(c, '')
    return s