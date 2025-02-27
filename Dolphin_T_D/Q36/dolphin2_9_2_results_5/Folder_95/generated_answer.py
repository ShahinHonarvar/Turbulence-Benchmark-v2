def filter_chars(s):
    for c in s[56:86]:
        if '+' < c < 'w':
            s = ''.join((ch for ch in s if ch != c))
    return s