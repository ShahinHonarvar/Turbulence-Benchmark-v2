def filter_chars(text):
    for i in range(114, 640):
        if i < len(text) and text[i] >= '!' and (text[i] <= 'x'):
            text = text.replace(text[i], '')
    return text