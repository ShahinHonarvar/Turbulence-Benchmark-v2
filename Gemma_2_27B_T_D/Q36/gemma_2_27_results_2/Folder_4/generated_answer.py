def filter_chars(text):
    for i in range(42, 67):
        char = text[i]
        if char > '6' and char < 'g':
            text = text.replace(char, '')
    return text