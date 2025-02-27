def filter_chars(text):
    for i in range(15, 85):
        if 'I' < text[i] < 'M':
            text = text.replace(text[i], '')
    return text