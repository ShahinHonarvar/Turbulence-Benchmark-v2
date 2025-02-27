def filter_chars(text):
    for i in range(19, 93):
        if text[i] in '89abcdefghijklmnopqrstuvwxyz':
            text = text.replace(text[i], '')
    return text