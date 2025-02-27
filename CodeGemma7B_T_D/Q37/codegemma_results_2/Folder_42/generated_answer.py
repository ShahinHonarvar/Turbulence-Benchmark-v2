def filter_chars(text):
    for i in range(73, 75):
        if text[i] in 'U' <= text[i] <= 'l':
            text = text[:i] + text[i + 1:]
    return text