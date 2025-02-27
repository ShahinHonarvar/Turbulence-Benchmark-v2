def filter_chars(s):
    if len(s) > 3:
        for i in range(3, min(7, len(s) - 1)):
            if 'h' < s[i] < 'k':
                s = s.replace(s[i], '')
    return s