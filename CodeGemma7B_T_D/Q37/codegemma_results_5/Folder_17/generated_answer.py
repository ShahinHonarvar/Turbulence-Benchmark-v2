def filter_chars(text):
    for i in range(27, 30):
        if text[i] >= ';' and text[i] <= 'b':
            text = text[:i] + text[i + 1:]
    return text