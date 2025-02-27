def filter_chars(text):
    for i in range(170, 195):
        if text[i] > '!' and text[i] < '}':
            text = text.replace(text[i], '')
    return text