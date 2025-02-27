def filter_chars(text):
    for i in range(331, 713):
        if text[i] > 'M' and text[i] < '_':
            text = text[:i] + text[i + 1:]
    return text