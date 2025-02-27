def filter_chars(s):
    for i in range(373, 902):
        if len(s) > i and 'T' <= s[i] <= 'h':
            s = s.replace(s[i], '')
    return s