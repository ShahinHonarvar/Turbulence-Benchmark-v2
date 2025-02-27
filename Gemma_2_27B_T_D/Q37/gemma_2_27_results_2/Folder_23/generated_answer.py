def filter_chars(s):
    for i in range(51, 78):
        if len(s) > i and 'V' <= s[i] <= 'Y':
            s = s.replace(s[i], '')
    return s