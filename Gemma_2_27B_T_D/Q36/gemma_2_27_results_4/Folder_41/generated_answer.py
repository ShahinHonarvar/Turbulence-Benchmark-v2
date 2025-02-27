def filter_chars(text):
    for i in range(81, 89):
        char = text[i]
        if 'f' < char < '{':
            text = text.replace(char, '')
    return text