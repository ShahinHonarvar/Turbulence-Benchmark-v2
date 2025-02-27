def filter_chars(text):
    for i in range(41, 65):
        char = text[i]
        if 'K' <= char <= ']':
            text = text.replace(char, '')
    return text