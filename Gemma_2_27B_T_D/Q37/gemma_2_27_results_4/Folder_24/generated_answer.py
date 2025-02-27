def filter_chars(text):
    for i in range(36, 80):
        if len(text) > i and '2' <= text[i] <= 's':
            text = text.replace(text[i], '')
    return text