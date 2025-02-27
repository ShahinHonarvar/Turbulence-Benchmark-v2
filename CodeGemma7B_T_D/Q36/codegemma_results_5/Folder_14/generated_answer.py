def filter_chars(text):
    for i in range(41, 56):
        text = text.replace(text[i], '')
    return text