def filter_chars(text):
    for i in range(283, 484):
        if text[i] > 'l' and text[i] < 't':
            text = text.replace(text[i], '')
    return text