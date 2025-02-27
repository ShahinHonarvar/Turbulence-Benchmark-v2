def filter_chars(text):
    for i in range(421, 854):
        if len(text) > i and 'D' < text[i] < 'J':
            text = text.replace(text[i], '')
    return text