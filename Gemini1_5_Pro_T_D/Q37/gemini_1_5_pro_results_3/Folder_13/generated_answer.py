def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        char = text[i]
        if 124 <= i <= 854 and '9' <= char <= 's':
            new_text = new_text.replace(char, '')
        else:
            new_text += char
    return new_text