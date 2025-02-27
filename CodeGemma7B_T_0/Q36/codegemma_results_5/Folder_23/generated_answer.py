def filter_chars(text):
    for i in range(21, 25):
        if text[i] > '5' and text[i] < '}':
            text = text.replace(text[i], '')
    return text