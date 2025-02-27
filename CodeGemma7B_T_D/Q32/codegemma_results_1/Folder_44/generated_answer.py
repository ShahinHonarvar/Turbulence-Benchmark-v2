def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'g':
            new_text += char + 'M'
        else:
            new_text += char
    return new_text