def filter_chars(s):
    for i in range(373, 902):
        if s[i] >= 'T' and s[i] <= 'h':
            s = s[:i] + s[i + 1:]
    return s