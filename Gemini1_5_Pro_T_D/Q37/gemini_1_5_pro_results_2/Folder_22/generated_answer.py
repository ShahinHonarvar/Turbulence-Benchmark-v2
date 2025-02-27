def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        char = text[i]
        if not (33 <= i <= 70 and '7' <= char <= 'k'):
            new_text += char
    return new_text