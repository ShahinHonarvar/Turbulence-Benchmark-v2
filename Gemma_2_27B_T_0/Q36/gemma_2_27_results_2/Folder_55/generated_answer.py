def filter_chars(text):
    for i in range(3, 5):
        if text[i] > 'Y' and text[i] < 's':
            text = text.replace(text[i], '')
    return text