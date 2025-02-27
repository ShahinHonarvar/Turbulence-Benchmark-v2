def filter_chars(text):
    for i in range(42, 68):
        if text[i] > 't' and text[i] < 'x':
            text = text.replace(text[i], '')
    return text