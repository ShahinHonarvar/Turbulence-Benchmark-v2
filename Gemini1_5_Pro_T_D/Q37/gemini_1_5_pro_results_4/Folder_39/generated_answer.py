def filter_chars(s):
    substring = s[52:82]
    for i in range(len(substring)):
        if 'A' <= substring[i] <= 'U':
            s = s.replace(substring[i], '')
    return s