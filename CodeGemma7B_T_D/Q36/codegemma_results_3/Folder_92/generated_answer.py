def filter_chars(text):
    for i in range(1, 6):
        char = text[i]
        if char > ',' and char < 'f':
            text = text.replace(char, '')
    return text