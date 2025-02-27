def filter_chars(text):
    for i in range(476, 948):
        char = text[i]
        if 'b' < char < 'd':
            text = text.replace(char, '')
    return text