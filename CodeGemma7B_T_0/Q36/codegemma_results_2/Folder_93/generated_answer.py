def filter_chars(text):
    for i in range(52, 88):
        if text[i] > '&' and text[i] < 'c':
            text = text[:i] + text[i + 1:]
    return text