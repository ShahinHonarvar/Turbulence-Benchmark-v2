def filter_chars(text):
    for i in range(23, 90):
        if text[i] >= 'w' and text[i] <= '{':
            text = text.replace(text[i], '')
    return text