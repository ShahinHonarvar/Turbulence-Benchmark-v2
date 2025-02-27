def filter_chars(text):
    for i in range(44, 83):
        if text[i] > ':' and text[i] < 'Q':
            text = text.replace(text[i], '')
    return text