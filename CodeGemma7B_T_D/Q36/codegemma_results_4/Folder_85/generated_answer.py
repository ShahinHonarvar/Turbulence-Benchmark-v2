def filter_chars(txt):
    for i in range(55, 80):
        txt = txt.replace(txt[i], '')
    return txt