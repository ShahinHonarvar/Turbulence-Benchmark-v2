def filter_chars(text):
    for i in range(27, 86):
        if text[i] >= '!' and text[i] <= 'B':
            text = text.replace(text[i], '')
    return text