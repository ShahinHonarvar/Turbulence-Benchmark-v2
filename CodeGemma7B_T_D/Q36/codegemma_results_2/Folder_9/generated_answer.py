def filter_chars(txt):
    for i in range(50, 92):
        c = txt[i]
        if ord(c) <= ord('Q') and ord(c) >= ord('A'):
            txt = txt.replace(c, '')
    return txt