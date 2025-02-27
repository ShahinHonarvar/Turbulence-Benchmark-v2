def filter_chars(text):
    for i in range(49, 56):
        char = text[i]
        if 'I' < char < 'a':
            text = text.replace(char, '')
    return text