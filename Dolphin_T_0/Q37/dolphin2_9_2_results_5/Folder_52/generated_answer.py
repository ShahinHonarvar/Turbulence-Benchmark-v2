def filter_chars(s):
    for i in range(54, 84):
        if 'j' <= s[i] <= 'v':
            s = s.replace(s[i], '')
    return s