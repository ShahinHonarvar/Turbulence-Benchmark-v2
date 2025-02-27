def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == 'R':
            new_text += 'V' + char
        else:
            new_text += char
    return new_text