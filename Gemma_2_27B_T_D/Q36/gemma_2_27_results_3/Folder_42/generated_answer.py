def filter_chars(text):
    for i in range(42, 68):
        if len(text) > i:
            if text[i] > 't' and text[i] < 'x':
                text = text.replace(text[i], '')
    return text