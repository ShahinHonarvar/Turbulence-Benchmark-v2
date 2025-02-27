def filter_chars(txt):
    for i in range(55, 80):
        if txt[i] > 'S' and txt[i] < 's':
            txt = txt.replace(txt[i], '')
    return txt