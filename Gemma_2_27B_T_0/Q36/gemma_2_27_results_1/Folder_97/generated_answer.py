def filter_chars(text):
    for i in range(309, 591):
        char = text[i]
        if 'S' < char < 'm':
            text = text.replace(char, '')
    return text