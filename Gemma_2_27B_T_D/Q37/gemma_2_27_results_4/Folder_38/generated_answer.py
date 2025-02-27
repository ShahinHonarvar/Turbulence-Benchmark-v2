def filter_chars(text):
    for i in range(24, 80):
        if len(text) > i and 'a' <= text[i] <= 'f':
            text = text.replace(text[i], '')
    return text