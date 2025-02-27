def filter_chars(text):
    for i in range(13, 40):
        if text[i] > ':' and text[i] < 'C':
            text = text.replace(text[i], '')
    return text