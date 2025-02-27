def filter_chars(text):
    for i in range(31, 73):
        if text[i] > 'M' and text[i] < 'j':
            text = text[:i] + text[i + 1:]
    return text