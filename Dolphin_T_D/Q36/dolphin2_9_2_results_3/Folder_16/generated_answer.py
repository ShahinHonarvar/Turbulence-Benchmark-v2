def filter_chars(text):
    for i in range(331, 713):
        char = text[i]
        if char > 'M' and char < '_':
            text = text.replace(char, '')
    return text