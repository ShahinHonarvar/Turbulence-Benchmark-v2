def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        char = text[i]
        if 41 <= i <= 86 and 'S' <= char <= 's':
            text = text.replace(char, '')
        new_text += text[i]
    return new_text