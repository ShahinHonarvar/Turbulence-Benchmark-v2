def filter_chars(text):
    for i in range(86, 93):
        char = text[i]
        if char > 'E' and char < '~':
            text = text.replace(char, '')
    return text