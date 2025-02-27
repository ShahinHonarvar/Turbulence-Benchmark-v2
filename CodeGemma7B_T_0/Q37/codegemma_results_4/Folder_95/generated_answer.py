def filter_chars(text):
    for i in range(35, 41):
        if text[i] in '()abcdefghijklmnopqrstuvwxyz':
            text = text.replace(text[i], '')
    return text