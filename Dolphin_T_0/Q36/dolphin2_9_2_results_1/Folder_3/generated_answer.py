def filter_chars(s):
    for i in range(42, 78):
        ch = s[i]
        if '!' < ch < '?':
            s = s.replace(ch, '')
    return s