def filter_chars(text):
    for i in range(43, 59):
        char = text[i]
        if '5' < char < 'C':
            text = text.replace(char, '')
    return text