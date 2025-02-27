def filter_chars(text):
    for i in range(344, 874):
        if text[i] > 'f' and text[i] < '~':
            text = text[:i] + text[i + 1:]
    return text