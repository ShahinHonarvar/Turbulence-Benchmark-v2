def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'N':
            new_text += char + 'z'
        else:
            new_text += char
    return new_text