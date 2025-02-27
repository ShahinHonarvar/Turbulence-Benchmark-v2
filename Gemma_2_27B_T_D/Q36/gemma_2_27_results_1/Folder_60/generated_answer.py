def filter_chars(text):
    for i in range(23, 83):
        char = text[i]
        if 'f' < char < 'o':
            text = text.replace(char, '')
    return text