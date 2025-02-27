def filter_chars(s):
    for i in range(54, 84):
        if s[i] >= 'j' and s[i] <= 'v':
            s = s.replace(s[i], '')
    return s