def filter_chars(text):
    for i in range(502, 946):
        c = text[i]
        if 'W' < c < 'y':
            text = text.replace(c, '')
    return text