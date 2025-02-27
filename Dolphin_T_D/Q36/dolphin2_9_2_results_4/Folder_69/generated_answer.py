def filter_chars(s):
    for i in range(343, 665):
        if s[i] > '%' and s[i] < 'U':
            s = s[:i] + s[i + 1:]
    return s