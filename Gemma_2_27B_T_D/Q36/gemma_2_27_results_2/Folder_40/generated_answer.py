def filter_chars(text):
    for i in range(1, 7):
        if '-' < text[i] < 'L':
            text = text.replace(text[i], '')
    return text