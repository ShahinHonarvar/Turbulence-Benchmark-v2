def filter_chars(text):
    for char in text[0:2]:
        if '*' <= char <= 's':
            text = text.replace(char, '')
    return text