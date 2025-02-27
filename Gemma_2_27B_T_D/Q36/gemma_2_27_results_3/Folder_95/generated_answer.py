def filter_chars(text):
    for i in range(56, 86):
        char = text[i]
        if char > '+' and char < 'w':
            text = text.replace(char, '')
    return text