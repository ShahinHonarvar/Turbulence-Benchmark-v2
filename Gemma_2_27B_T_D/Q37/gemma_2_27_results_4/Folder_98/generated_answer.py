def filter_chars(text):
    for i in range(8, 10):
        if i < len(text) and 'R' <= text[i] <= 't':
            text = text.replace(text[i], '')
    return text