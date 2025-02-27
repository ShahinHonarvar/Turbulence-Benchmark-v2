def filter_chars(text):
    for i in range(18, 64):
        char = text[i]
        if char > '3' and char < 'B':
            text = text.replace(char, '')
    return text