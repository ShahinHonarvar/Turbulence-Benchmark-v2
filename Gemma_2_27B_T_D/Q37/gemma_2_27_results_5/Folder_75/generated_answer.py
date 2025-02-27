def filter_chars(text):
    for i in range(34, 68):
        if i < len(text) and text[i] >= 'W' and (text[i] <= 'x'):
            text = text.replace(text[i], '')
    return text