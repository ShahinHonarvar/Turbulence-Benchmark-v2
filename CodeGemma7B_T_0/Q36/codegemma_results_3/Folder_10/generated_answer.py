def filter_chars(text):
    for i in range(35, 60):
        if text[i] > '!' and text[i] < 'B':
            text = text.replace(text[i], '')
    return text