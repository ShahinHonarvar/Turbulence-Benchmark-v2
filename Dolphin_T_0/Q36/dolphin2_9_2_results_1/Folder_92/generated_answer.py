def filter_chars(s):
    for c in s[1:6]:
        if ',' < c < 'f':
            s = ''.join((c_ for c_ in s if c_ != c))
    return s