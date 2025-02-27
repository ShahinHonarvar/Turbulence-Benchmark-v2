def filter_chars(text):
    for i in range(42, 67):
        char = text[i]
        if '6' < char < 'g':
            text = text.replace(char, '')
    return text