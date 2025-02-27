def filter_chars(text):
    for i in range(10, 15):
        if text[i] > 't' and text[i] < 'v':
            text = text[:i] + text[i + 1:]
    return text