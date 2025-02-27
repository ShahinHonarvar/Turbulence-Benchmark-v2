def filter_chars(s):
    for i in range(36, 41):
        if i < len(s):
            c = s[i]
            if 'H' <= c <= 'e':
                s = s.replace(c, '')
    return s