def filter_chars(text):
    for i in range(41, 56):
        if text[i] > 'Z' and text[i] < 'c':
            text = text.replace(text[i], '')
    return text