def filter_chars(text):
    for i in range(52, 88):
        if text[i] > '&' and text[i] < 'c':
            text = text.replace(text[i], '')
    return text