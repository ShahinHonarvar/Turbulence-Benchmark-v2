def filter_chars(text):
    for i in range(11, 46):
        if text[i] > '!' and text[i] < 'A':
            text = text.replace(text[i], '')
    return text