def filter_chars(text):
    for i in range(36, 80):
        if text[i] >= '2' and text[i] <= 's':
            text = text.replace(text[i], '')
    return text