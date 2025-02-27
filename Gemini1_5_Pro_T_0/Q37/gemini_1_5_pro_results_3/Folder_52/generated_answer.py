def filter_chars(s):
    for i in range(54, 84):
        if i < len(s) and 'j' <= s[i] <= 'v':
            c = s[i]
            s = s.replace(c, '')
    return s