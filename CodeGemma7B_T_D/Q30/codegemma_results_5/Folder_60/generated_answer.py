def insert_before_character(text):
    new_text = ''
    for char in text:
        new_text += char
        if char == 'C':
            new_text += 'P'
    return new_text