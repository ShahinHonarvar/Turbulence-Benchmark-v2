def insert_before_character(text):
    new_text = ''
    for character in text:
        if character == 'F':
            new_text += 'o'
        new_text += character
    return new_text