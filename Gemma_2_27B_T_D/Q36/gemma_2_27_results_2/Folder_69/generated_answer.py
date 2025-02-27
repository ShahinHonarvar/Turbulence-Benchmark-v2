def filter_chars(text):
    for i in range(343, 665):
        char = text[i]
        if '%' < char < 'U':
            text = text.replace(char, '')
    return text