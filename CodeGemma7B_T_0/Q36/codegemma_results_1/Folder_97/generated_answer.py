def filter_chars(text):
    for i in range(309, 591):
        if text[i] > 'S' and text[i] < 'm':
            text = text.replace(text[i], '')
    return text