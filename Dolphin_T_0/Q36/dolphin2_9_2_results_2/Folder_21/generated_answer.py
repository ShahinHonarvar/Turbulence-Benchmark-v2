def filter_chars(s):
    for c in s[219:403]:
        if '*' < c < '7':
            s = s.replace(c, '')
    return s