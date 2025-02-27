def filter_chars(text):
    for i in range(32, 61):
        if text[i] > '3' and text[i] < 'D':
            text = text.replace(text[i], '')
    return text