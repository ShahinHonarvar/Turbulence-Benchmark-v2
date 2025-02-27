def filter_chars(text):
    for i in range(49, 56):
        if text[i] > 'I' and text[i] < 'a':
            text = text.replace(text[i], '')
    return text