def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'Q':
            new_text += char + 'I'
        else:
            new_text += char
    return new_text