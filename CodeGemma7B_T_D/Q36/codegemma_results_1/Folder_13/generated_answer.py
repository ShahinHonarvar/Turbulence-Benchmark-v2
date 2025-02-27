def filter_chars(txt):
    for i in range(323, 526):
        if txt[i] > ')' and txt[i] < 'O':
            txt = txt.replace(txt[i], '')
    return txt