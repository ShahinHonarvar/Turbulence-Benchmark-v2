def filter_chars(text):
    for i in range(31, 50):
        if text[i] > '/' and text[i] < 'J':
            text = text.replace(text[i], '')
    return text