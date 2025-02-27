def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == '6':
            new_text += '9' + char
        else:
            new_text += char
    return new_text