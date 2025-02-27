def filter_chars(text):
    for i in range(722, 833):
        if i < len(text) and text[i] >= 'K' and (text[i] <= 'm'):
            text = text.replace(text[i], '')
    return text