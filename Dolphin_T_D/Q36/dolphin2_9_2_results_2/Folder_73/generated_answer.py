def filter_chars(text):
    for i in range(66, 90):
        if '#' < text[i] < 'T':
            text = text.replace(text[i], '')
    return text