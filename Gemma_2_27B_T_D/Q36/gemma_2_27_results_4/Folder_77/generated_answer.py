def filter_chars(text):
    for i in range(221, 419):
        char = text[i]
        if char > '-' and char < 'v':
            text = text.replace(char, '')
    return text