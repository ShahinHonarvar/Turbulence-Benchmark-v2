def filter_chars(text):
    for i in range(318, 337):
        char = text[i]
        if 'B' < char < 'z':
            text = text.replace(char, '')
    return text