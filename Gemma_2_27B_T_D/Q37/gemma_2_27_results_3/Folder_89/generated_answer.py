def filter_chars(text):
    for i in range(11, 33):
        if len(text) > i and text[i] >= '!' and (text[i] <= '@'):
            text = text.replace(text[i], '')
    return text