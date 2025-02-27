def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        char = text[i]
        if 36 <= i <= 79 and '2' <= char <= 's':
            new_text = new_text.replace(char, '')
        else:
            new_text += char
    return new_text