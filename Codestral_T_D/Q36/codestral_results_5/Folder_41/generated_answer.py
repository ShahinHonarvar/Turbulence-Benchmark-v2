def filter_chars(text):
    for char in text[81:89]:
        if 'f' < char < '{':
            text = text.replace(char, '')
    return text