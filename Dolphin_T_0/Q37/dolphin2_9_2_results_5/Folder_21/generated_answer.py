def filter_chars(txt):
    for char in txt:
        if 603 <= txt.index(char) <= 759 and 'Q' <= char <= 'h':
            txt = txt.replace(char, '')
    return txt