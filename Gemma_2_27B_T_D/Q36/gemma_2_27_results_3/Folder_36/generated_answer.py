def filter_chars(text):
    for i in range(283, 484):
        c = text[i]
        if 'l' < c < 't':
            text = text.replace(c, '')
    return text