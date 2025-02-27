def filter_chars(text):
    for i in range(31, 70):
        if text[i] > 'B' and text[i] < 'v':
            text = text.replace(text[i], '')
    return text