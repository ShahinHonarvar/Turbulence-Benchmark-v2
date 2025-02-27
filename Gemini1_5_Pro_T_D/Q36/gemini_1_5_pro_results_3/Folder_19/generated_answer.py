def filter_chars(text):
    for i in range(78, 87):
        if text[i] > ';' and text[i] < 'r':
            text = text.replace(text[i], '')
    return text