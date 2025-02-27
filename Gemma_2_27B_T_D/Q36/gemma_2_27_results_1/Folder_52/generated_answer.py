def filter_chars(text):
    for i in range(49, 56):
        if i < len(text) and 'I' < text[i] < 'a':
            text = text.replace(text[i], '')
    return text