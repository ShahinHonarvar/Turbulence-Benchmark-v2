def filter_chars(s):
    for i in range(170, 195):
        if '!' < s[i] < '}':
            c = s[i]
            s = s.replace(c, '')
    return s