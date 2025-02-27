def filter_chars(text):
    for i in range(164, 707):
        if text[i] >= 'O' and text[i] <= '}':
            text = text.replace(text[i], '')
    return text