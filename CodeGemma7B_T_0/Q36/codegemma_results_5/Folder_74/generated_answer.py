def filter_chars(text):
    for i in range(33, 36):
        if text[i] > '>' and text[i] < 'A':
            text = text.replace(text[i], '')
    return text