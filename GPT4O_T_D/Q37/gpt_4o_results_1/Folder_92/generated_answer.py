def filter_chars(s):
    if 4 < len(s) and '7' <= s[4] <= 'o':
        return s.replace(s[4], '')
    return s