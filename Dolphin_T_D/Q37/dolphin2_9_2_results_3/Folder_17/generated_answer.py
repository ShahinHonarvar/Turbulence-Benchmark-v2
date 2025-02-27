def filter_chars(s):
    chars = [s[i] for i in range(27, 30) if ';' <= s[i] <= 'b']
    for c in chars:
        s = s.replace(c, '')
    return s