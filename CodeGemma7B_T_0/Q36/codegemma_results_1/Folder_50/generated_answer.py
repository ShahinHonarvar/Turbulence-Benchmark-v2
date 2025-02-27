def filter_chars(text):
    for i in range(61, 88):
        if text[i] > '%' and text[i] < 'q':
            text = text.replace(text[i], '')
    return text