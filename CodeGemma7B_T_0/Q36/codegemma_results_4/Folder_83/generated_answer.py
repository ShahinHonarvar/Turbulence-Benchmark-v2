def filter_chars(text):
    for i in range(72, 93):
        if text[i] > '<' and text[i] < 'J':
            text = text[:i] + text[i + 1:]
    return text