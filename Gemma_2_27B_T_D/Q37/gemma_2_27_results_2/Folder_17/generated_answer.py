def filter_chars(s):
    for i in range(27, 30):
        if i < len(s):
            for c in s[i:]:
                if c >= ';' and c <= 'b':
                    s = s.replace(c, '')
    return s