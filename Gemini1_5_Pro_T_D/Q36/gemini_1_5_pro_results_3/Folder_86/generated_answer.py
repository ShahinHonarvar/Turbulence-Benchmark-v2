def filter_chars(s):
    for i in range(672, 709):
        if i < len(s) and s[i] > 'X' and (s[i] < '}'):
            c = s[i]
            s = s.replace(c, '')
    return s