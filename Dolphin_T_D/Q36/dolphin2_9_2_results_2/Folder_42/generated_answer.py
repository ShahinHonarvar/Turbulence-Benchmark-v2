def filter_chars(txt):
    for ch in txt[42:68]:
        if 't' < ch < 'x':
            txt = txt.replace(ch, '')
    return txt