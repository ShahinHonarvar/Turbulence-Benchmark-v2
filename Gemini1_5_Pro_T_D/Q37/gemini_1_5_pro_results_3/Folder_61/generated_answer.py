def filter_chars(text):
    for i in range(5, 7):
        if i < len(text):
            c = text[i]
            if 'G' <= c <= 'p':
                text = text.replace(c, '')
    return text