def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'T':
            new_text += char + ' '
        else:
            new_text += char
    return new_text