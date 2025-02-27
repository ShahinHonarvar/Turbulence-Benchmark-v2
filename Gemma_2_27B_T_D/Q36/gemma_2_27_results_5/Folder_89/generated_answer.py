def filter_chars(text):
    for i in range(57, 69):
        char = text[i]
        if char > '(' and char < 'W':
            text = text.replace(char, '')
    return text