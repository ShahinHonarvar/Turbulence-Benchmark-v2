def filter_chars(s):
    for i in range(18, 95):
        if i < len(s) and s[i] > 'K' and (s[i] < 'a'):
            s = s.replace(s[i], '')
    return s