def filter_chars(s):
    s = list(s)
    for i in range(373, 902):
        if 'T' <= s[i] <= 'h':
            while s[i] in s:
                s.remove(s[i])
    return ''.join(s)