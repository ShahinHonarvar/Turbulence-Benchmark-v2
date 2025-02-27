def filter_chars(txt):
    for i in range(14, 75):
        if txt[i] > '9' and txt[i] < 'K':
            txt = txt.replace(txt[i], '')
    return txt