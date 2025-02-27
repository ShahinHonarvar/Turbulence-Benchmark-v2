def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'o':
            new_text += char + 'O'
        else:
            new_text += char
    return new_text