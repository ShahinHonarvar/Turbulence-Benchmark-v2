def filter_chars(s):
    for c in s:
        if c >= '_' and c <= 'o':
            if 71 <= s.index(c) <= 96:
                s = s.replace(c, '')
    return s