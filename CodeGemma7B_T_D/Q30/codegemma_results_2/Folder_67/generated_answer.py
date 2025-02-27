def insert_before_character(text):
    new_text = ''
    for char in text:
        if char == 'j':
            new_text += '1j'
        else:
            new_text += char
    return new_text