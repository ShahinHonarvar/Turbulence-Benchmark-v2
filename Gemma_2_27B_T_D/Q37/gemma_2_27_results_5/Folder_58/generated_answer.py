def filter_chars(text):
    for i in range(503, 754):
        if len(text) > i and '9' <= text[i] <= 'w':
            text = text.replace(text[i], '')
    return text