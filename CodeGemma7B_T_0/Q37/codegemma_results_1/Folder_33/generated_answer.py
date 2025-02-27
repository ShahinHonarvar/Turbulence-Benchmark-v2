def filter_chars(text):
    for i in range(722, 833):
        if text[i] >= 'K' and text[i] <= 'm':
            text = text[:i] + text[i + 1:]
    return text