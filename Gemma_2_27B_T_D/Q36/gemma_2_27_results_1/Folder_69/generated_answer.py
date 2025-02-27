def filter_chars(text):
    for i in range(343, 665):
        if text[i] > '%' and text[i] < 'U':
            text = text.replace(text[i], '')
    return text