def filter_chars(text):
    for i in range(29, 33):
        if text[i] > '%' and text[i] < 'a':
            text = text.replace(text[i], '')
    return text