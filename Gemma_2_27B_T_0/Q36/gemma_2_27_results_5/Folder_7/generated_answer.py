def filter_chars(text):
    for i in range(502, 946):
        if text[i] > 'W' and text[i] < 'y':
            text = text.replace(text[i], '')
    return text