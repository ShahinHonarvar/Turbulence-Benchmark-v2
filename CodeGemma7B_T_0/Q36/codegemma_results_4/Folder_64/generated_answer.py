def filter_chars(text):
    for i in range(1, 7):
        if text[i] > '3' and text[i] < '^':
            text = text.replace(text[i], '')
    return text