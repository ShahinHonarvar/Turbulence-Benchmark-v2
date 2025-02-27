def insert_after_character(text):
    new_text = ''
    for char in text:
        if char == 'e':
            new_text += char + '0'
        else:
            new_text += char
    return new_text