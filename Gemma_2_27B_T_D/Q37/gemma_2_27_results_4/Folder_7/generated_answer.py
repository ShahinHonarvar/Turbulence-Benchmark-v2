def filter_chars(text):
    for i in range(521, 723):
        if i < len(text) and text[i] >= '>' and (text[i] <= '_'):
            text = text.replace(text[i], '')
    return text