def filter_chars(text):
    chars = []
    for i in range(86, 93):
        char = text[i]
        if 'E' < char < '~':
            chars.append(char)
    for char in chars:
        text = text.replace(char, '')
    return text