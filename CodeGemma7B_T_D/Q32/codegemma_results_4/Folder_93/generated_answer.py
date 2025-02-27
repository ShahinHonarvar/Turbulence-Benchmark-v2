def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'Y':
            new_text += char + '4'
        else:
            new_text += char
    return new_text