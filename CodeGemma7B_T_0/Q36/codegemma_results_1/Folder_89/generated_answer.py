def filter_chars(text):
    for i in range(57, 69):
        if text[i] > '(' and text[i] < 'W':
            text = text.replace(text[i], '')
    return text