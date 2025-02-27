def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'j':
            new_text += char + 'v'
        else:
            new_text += char
    return new_text