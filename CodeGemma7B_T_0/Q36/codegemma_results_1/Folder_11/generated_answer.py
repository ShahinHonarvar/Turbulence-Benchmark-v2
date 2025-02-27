def filter_chars(text):
    for i in range(86, 93):
        if text[i] > 'E' and text[i] < '~':
            text = text.replace(text[i], '')
    return text