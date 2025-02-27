def filter_chars(text):
    for i in range(41, 56):
        char = text[i]
        if 'Z' < char < 'c':
            text = text.replace(char, '')
    return text