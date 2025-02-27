def insert_after_character(text):
    new_text = ''
    for character in text:
        if character == 'U':
            new_text += character + 'U'
        else:
            new_text += character
    return new_text