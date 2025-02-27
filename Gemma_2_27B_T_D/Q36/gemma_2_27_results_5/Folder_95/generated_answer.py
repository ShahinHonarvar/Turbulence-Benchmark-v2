def filter_chars(text):
    for i in range(56, 86):
        if text[i] > '+' and text[i] < 'w':
            text = text.replace(text[i], '')
    return text