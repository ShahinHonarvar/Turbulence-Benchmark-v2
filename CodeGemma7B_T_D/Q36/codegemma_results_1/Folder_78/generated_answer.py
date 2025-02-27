def filter_chars(text):
    for i in range(29, 33):
        text = text.replace(text[i], '')
    return text