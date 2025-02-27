def filter_chars(text):
    for i in range(1, 6):
        for char in text[i]:
            if '$' <= char <= ';':
                text = text.replace(char, '')
    return text