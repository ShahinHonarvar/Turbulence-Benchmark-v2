def filter_chars(text):
    for i in range(78, 81):
        if text[i] > 'S' and text[i] < '[':
            text = text.replace(text[i], '')
    return text