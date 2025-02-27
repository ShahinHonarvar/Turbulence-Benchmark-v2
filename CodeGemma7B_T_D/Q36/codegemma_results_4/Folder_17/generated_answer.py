def filter_chars(text):
    for i in range(18, 95):
        if text[i] > 'K' and text[i] < 'a':
            text = text[:i] + text[i + 1:]
    return text