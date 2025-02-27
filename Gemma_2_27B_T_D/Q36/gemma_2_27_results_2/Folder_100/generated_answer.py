def filter_chars(text):
    for i in range(43, 69):
        char = text[i]
        if 'B' < char < 'r':
            text = text.replace(char, '')
    return text