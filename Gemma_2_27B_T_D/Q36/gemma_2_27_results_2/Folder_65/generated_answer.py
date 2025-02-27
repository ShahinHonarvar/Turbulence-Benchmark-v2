def filter_chars(text):
    for i in range(58, 82):
        char = text[i]
        if 'F' < char < 'O':
            text = text.replace(char, '')
    return text