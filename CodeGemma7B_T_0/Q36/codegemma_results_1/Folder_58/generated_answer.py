def filter_chars(text):
    for i in range(318, 337):
        if text[i] > 'B' and text[i] < 'z':
            text = text.replace(text[i], '')
    return text