def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'R':
            new_text += char
            new_text += 'V'
        else:
            new_text += char
    return new_text