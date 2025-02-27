def filter_chars(text):
    for i in range(44, 59):
        char = text[i]
        if char > '/' and char < '6':
            text = text.replace(char, '')
    return text