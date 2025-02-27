def filter_chars(text):
    for i in range(3, 5):
        if len(text) > i and 'Y' < text[i] < 's':
            text = text.replace(text[i], '')
    return text