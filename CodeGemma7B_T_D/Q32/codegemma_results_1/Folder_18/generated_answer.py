def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'K':
            new_text += char + 'l'
        else:
            new_text += char
    return new_text