def filter_chars(text):
    for i in range(26, 80):
        text = text.replace(text[i], '')
    return text