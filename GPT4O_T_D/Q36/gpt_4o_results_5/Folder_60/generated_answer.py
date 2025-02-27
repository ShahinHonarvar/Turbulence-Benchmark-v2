def filter_chars(s):
    if len(s) <= 23:
        return s
    to_remove = set(s[24:83])
    for ch in list(to_remove):
        if 'f' < ch < 'o':
            s = s.replace(ch, '')
    return s