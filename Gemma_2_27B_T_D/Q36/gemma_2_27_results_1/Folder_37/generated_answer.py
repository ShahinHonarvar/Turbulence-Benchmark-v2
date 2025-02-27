def filter_chars(text):
    for i in range(44, 59):
        c = text[i]
        if c > '/' and c < '6':
            text = text.replace(c, '')
    return text