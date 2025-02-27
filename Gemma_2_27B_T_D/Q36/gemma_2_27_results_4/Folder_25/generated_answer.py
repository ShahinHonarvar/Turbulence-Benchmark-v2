def filter_chars(text):
    for i in range(24, 37):
        if 'A' < text[i] < 'h':
            text = text.replace(text[i], '')
    return text