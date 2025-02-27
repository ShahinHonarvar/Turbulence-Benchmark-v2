def filter_chars(text):
    for i in range(51, 76):
        if text[i] > '5' and text[i] < 'f':
            text = text.replace(text[i], '')
    return text