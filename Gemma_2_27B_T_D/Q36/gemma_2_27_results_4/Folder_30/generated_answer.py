def filter_chars(text):
    for i in range(23, 45):
        if len(text) > i and '3' < text[i] < 'I':
            text = text.replace(text[i], '')
    return text