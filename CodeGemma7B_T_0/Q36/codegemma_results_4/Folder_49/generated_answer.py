def filter_chars(text):
    for i in range(46, 91):
        if text[i] > 'D' and text[i] < 'H':
            text = text[:i] + text[i + 1:]
    return text