def filter_chars(text):
    for i in range(344, 874):
        char = text[i]
        if 'f' < char < '~':
            text = text.replace(char, '')
    return text