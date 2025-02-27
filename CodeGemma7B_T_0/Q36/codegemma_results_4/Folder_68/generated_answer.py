def filter_chars(text):
    for i in range(1, 9):
        if text[i] > '8' and text[i] < 'm':
            text = text.replace(text[i], '')
    return text