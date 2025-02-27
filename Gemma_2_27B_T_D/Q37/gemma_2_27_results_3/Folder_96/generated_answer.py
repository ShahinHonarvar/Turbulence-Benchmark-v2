def filter_chars(text):
    for i in range(86, 93):
        if len(text) > i and text[i] >= '!' and (text[i] <= 's'):
            text = text.replace(text[i], '')
    return text