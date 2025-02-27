def filter_chars(text):
    for i in range(14, 75):
        if text[i] > '9' and text[i] < 'K':
            text = text.replace(text[i], '')
    return text