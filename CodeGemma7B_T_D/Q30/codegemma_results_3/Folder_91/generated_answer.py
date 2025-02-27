def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == 'a':
            new_text += '0' + char
        else:
            new_text += char
    return new_text