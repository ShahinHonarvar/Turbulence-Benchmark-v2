def filter_chars(text):
    for i in range(70, 74):
        if i < len(text) and text[i] > 'A' and (text[i] < 'U'):
            text = text.replace(text[i], '')
    return text