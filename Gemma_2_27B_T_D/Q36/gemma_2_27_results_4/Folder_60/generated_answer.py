def filter_chars(text):
    for i in range(23, 83):
        if len(text) > i and 'f' < text[i] < 'o':
            text = text.replace(text[i], '')
    return text