def filter_chars(text):
    for i in range(13, 29):
        if i < len(text):
            char = text[i]
            if 'c' <= char <= 'n':
                text = text.replace(char, '')
    return text