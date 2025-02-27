def filter_chars(text):
    for i in range(83, 100):
        char = text[i]
        if '*' <= char <= 'j':
            text = text.replace(char, '')
    return text