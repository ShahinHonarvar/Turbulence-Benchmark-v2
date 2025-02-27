def filter_chars(text):
    for i in range(43, 69):
        if text[i] > 'B' and text[i] < 'r':
            text = text.replace(text[i], '')
    return text