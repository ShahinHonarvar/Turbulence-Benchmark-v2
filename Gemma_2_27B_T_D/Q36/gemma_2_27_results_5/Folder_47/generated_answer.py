def filter_chars(text):
    for i in range(45, 57):
        char = text[i]
        if 'F' < char < 'n':
            text = text.replace(char, '')
    return text