def filter_chars(text):
    for i in range(44, 68):
        char = text[i]
        if 'W' < char < 'x':
            text = text.replace(char, '')
    return text