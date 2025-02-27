def filter_chars(txt):
    new_txt = ''
    for i in range(23, 83):
        if not (txt[i] > 'f' and txt[i] < 'o'):
            new_txt += txt[i]
    return new_txt