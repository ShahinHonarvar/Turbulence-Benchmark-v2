def filter_chars(text):
    for i in range(35, 60):
        if text[i] > '!' and text[i] < 'B':
            text = text[:i] + text[i + 1:]
    return text