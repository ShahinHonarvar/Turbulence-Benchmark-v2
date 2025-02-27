def filter_chars(text):
    for i in range(4, 8):
        if '1' < text[i] < 'J':
            text = text.replace(text[i], '')
    return text