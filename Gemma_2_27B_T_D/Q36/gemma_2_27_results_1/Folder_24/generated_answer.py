def filter_chars(text):
    for i in range(10, 15):
        if i < len(text) and text[i] > 't' and (text[i] < 'v'):
            text = text.replace(text[i], '')
    return text