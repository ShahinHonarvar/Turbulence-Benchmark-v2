def filter_chars(text):
    for i in range(15, 85):
        if len(text) > i and 'I' < text[i] < 'M':
            text = text.replace(text[i], '')
    return text