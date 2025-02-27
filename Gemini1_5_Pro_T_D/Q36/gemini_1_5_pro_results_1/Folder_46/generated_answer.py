def filter_chars(text):
    new_text = ''
    for i in range(len(text)):
        char = text[i]
        if 19 < i < 69 and '<' < char < 'C':
            new_text = new_text.replace(char, '')
        else:
            new_text += char
    return new_text