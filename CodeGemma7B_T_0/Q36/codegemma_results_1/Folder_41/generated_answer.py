def filter_chars(text):
    for i in range(81, 89):
        if text[i] > 'f' and text[i] < '{':
            text = text.replace(text[i], '')
    return text