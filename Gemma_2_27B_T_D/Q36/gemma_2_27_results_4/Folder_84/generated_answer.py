def filter_chars(text):
    for i in range(171, 636):
        char = text[i]
        if 'c' < char < 's':
            text = text.replace(char, '')
    return text