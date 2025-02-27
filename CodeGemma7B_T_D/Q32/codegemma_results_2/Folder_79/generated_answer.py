def insert_after_character(text):
    new_text = ''
    for character in text:
        if character == 'E':
            new_text += character + 'E'
        else:
            new_text += character
    return new_text