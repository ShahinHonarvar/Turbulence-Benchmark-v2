def filter_chars(text):
    for i in range(55, 84):
        if text[i] > ';' and text[i] < 'z':
            text = text.replace(text[i], '')
    return text