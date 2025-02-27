def filter_chars(text):
    for i in range(46, 74):
        if text[i] > '&' and text[i] < 'M':
            text = text.replace(text[i], '')
    return text