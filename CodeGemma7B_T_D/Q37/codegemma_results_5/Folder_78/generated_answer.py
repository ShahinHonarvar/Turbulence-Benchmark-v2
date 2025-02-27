def filter_chars(txt):
    for i in range(75, 100):
        if txt[i] >= '8' and txt[i] <= 'e':
            txt = txt.replace(txt[i], '', txt.count(txt[i]))
    return txt