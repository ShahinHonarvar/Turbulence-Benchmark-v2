def filter_chars(s):
    for i in range(3, len(s) - 2):
        if 'h' < s[i] < 'k':
            s = s.replace(s[i], '')
    return s