def filter_chars(text):
    for i in range(7, 10):
        if i < len(text):
            char = text[i]
            if '6' <= char <= 'w':
                text = text.replace(char, '')
    return text