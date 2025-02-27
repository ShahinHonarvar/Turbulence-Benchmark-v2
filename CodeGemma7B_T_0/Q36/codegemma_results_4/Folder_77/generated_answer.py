def filter_chars(text):
    for i in range(221, 419):
        if text[i] > '-' and text[i] < 'v':
            text = text.replace(text[i], '')
    return text