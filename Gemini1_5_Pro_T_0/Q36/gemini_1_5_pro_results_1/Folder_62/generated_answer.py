def filter_chars(text):
    for i in range(63, 89):
        if text[i] > '*' and text[i] < 'w':
            text = text.replace(text[i], '')
    return text