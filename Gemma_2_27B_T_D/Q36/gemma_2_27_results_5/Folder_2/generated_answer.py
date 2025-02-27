def filter_chars(text):
    for i in range(421, 854):
        if text[i] > 'D' and text[i] < 'J':
            text = text.replace(text[i], '')
    return text