def insert_after_character(text):
    new_text = ''
    for character in text:
        new_text += character
        if character == ' ':
            new_text += 'H'
    return new_text