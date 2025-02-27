def filter_chars(text):
    for i in range(69, 87):
        text = text.replace(text[i], '')
    return text