def filter_chars(text):
    for i in range(171, 636):
        if 'c' < text[i] < 's':
            text = text.replace(text[i], '')
    return text