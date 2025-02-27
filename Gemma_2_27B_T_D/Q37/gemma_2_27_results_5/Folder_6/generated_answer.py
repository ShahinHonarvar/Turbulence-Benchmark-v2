def filter_chars(text):
    for i in range(13, 29):
        if len(text) > i and 'c' <= text[i] <= 'n':
            text = text.replace(text[i], '')
    return text