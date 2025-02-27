def filter_chars(text):
    for i in range(10, 79):
        if '?' < text[i] < 'm':
            text = text.replace(text[i], '')
    return text