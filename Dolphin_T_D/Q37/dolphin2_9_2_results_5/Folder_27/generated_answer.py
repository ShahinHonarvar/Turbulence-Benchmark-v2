def filter_chars(txt):
    for i in range(43, 81):
        if '=' <= txt[i] <= 'E':
            txt = txt.replace(txt[i], '')
    return txt