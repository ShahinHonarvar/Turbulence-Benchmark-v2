def filter_chars(text):
    for i in range(19, 34):
        if len(text) > i and 'S' <= text[i] <= '{':
            text = text.replace(text[i], '')
    return text