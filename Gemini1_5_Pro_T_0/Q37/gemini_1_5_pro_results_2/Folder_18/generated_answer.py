def filter_chars(s):
    for i in range(770, 971):
        if i < len(s) and '-' <= s[i] <= 'D':
            c = s[i]
            s = s.replace(c, '')
    return s