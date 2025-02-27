def filter_chars(s):
    if len(s) <= 25:
        return s
    for ch in s[25:37]:
        if 'A' < ch < 'h':
            s = s.replace(ch, '')
    return s