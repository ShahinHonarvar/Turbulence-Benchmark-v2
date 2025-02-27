def filter_chars(s):
    for i in range(259, 503):
        if i < len(s) and ',' <= s[i] <= '3':
            c = s[i]
            s = s.replace(c, '')
    return s