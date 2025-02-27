def filter_chars(s):
    for i in range(51, 78):
        if 'V' <= s[i] <= 'Y':
            s = s[:i] + s[i + 1:]
    return s