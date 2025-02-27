def filter_chars(text):
    for i in range(81, 86):
        if text[i] > '!' and text[i] < 's':
            text = text.replace(text[i], '')
    return text