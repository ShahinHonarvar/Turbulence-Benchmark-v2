def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'H':
            new_text += char + 's'
        else:
            new_text += char
    return new_text