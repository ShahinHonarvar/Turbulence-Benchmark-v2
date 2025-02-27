def filter_chars(text):
    for char in text[14:75]:
        if '9' < char < 'K':
            text = text.replace(char, '')
    return text