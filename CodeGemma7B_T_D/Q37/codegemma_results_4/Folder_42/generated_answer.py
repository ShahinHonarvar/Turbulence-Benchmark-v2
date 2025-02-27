def filter_chars(text):
    for i in range(73, 75 + 1):
        if text[i] >= 'U' and text[i] <= 'l':
            text = text.replace(text[i], '')
    return text