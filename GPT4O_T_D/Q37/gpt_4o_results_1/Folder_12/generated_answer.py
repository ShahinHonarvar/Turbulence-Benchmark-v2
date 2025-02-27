def filter_chars(s):
    if len(s) < 20:
        return s
    for i in range(19, min(91, len(s))):
        if 'F' <= s[i] <= 'h':
            s = s.replace(s[i], '')
    return s