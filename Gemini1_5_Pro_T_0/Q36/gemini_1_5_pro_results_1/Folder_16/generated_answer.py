def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        char = text[i]
        if 331 < i < 713 and 'M' < char < '_':
            continue
        new_text += char
    return new_text