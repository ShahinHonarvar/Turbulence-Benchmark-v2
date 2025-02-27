def filter_chars(text):
    for i in range(36, 80):
        if len(text) > i and 'a' <= text[i] <= 'i':
            text = text.replace(text[i], '')
    return text