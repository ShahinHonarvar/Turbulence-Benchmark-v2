def filter_chars(text):
    for i in range(3, 8):
        if '?' < text[i] < 'k':
            text = text.replace(text[i], '')
    return text