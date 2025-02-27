def filter_chars(text):
    for i in range(21, 25):
        if '5' < text[i] < '}':
            text = text.replace(text[i], '')
    return text