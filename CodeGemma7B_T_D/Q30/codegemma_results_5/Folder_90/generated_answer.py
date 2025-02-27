def insert_before_character(txt):
    for i in reversed(range(len(txt))):
        if txt[i] == 'U':
            txt = txt[:i] + 'F' + txt[i:]
    return txt