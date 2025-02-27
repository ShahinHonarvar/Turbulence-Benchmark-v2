def filter_chars(text):
    for i in range(669, 888):
        if text[i] > 'B' and text[i] < 'Y':
            text = text.replace(text[i], '')
    return text