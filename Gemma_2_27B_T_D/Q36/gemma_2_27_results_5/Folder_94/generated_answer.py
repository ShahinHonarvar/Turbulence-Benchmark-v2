def filter_chars(text):
    for i in range(15, 85):
        char = text[i]
        if 'I' < char < 'M':
            text = text.replace(char, '')
    return text