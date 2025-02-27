def filter_chars(s):
    for c in range(81, 89):
        if s[c] > 'f' and s[c] < '{':
            s = s.replace(s[c], '')
    return s