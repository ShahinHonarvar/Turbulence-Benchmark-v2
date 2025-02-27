def filter_chars(text):
    for i in range(18, 64):
        if text[i] > '3' and text[i] < 'B':
            text = text.replace(text[i], '')
    return text