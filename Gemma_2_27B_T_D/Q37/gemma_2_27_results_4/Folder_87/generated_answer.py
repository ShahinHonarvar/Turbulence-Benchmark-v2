def filter_chars(text):
    for i in range(18, 82):
        if 'W' <= text[i] <= '[':
            text = text.replace(text[i], '')
    return text