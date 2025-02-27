def filter_chars(s):
    s = list(s)
    for i, c in enumerate(s):
        if 15 <= i <= 55 and c >= 'W' and (c <= '{'):
            s.pop(i)
    return ''.join(s)