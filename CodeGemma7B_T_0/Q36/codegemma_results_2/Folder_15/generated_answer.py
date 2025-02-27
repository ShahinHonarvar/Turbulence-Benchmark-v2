def filter_chars(text):
    for i in range(2, 7):
        if text[i] > 'h' and text[i] < 'k':
            text = text.replace(text[i], '')
    return text