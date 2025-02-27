def filter_chars(text):
    for i in range(43, 59):
        if text[i] > '5' and text[i] < 'C':
            text = text.replace(text[i], '')
    return text