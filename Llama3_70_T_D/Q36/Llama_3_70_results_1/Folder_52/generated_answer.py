def filter_chars(s):
    res = ''
    for i, c in enumerate(s):
        if (i < 49 or i >= 56) or not 'I' < c < 'a':
            res += c
    return res