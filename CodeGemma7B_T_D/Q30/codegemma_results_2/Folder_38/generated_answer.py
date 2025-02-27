def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == 'X':
            new_text += '6' + char
        else:
            new_text += char
    return new_text