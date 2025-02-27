def filter_chars(text):
    for i in range(502, 946):
        char = text[i]
        if 'W' < char < 'y':
            text = text.replace(char, '')
    return text