def filter_chars(text):
    for i in range(23, 45):
        if text[i] > '3' and text[i] < 'I':
            text = text.replace(text[i], '')
    return text