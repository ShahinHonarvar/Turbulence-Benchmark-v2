def insert_after_character(text):
    new_text = ''
    for character in text:
        if character == 'b':
            new_text += character + 'y'
        else:
            new_text += character
    return new_text