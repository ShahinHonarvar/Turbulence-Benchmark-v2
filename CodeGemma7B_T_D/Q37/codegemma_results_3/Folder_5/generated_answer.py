def filter_chars(txt):
    for i in txt[24:82]:
        while i >= '5' and i <= '<':
            txt = txt.replace(i, '')
    return txt