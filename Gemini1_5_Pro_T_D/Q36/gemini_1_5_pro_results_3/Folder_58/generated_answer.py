def filter_chars(text):
    for i in range(318, 337):
        c = text[i]
        if 'B' < c < 'z':
            text = text.replace(c, '')
    return text