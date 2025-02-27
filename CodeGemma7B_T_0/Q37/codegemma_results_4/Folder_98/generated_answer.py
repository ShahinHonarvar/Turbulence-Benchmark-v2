def filter_chars(text):
    for i in range(8, 10):
        if text[i] >= 'R' and text[i] <= 't':
            text = text[:i] + text[i + 1:]
    return text