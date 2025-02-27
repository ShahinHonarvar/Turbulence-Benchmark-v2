def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'C':
            new_text += char + 'H'
        else:
            new_text += char
    return new_text