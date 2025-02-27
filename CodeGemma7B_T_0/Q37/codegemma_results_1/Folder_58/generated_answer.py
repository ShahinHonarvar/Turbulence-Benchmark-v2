def filter_chars(text):
    for i in range(503, 754):
        if text[i] >= '9' and text[i] <= 'w':
            text = text[:i] + text[i + 1:]
    return text