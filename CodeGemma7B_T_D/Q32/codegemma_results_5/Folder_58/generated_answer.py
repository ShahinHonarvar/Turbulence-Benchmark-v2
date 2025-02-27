def insert_after_character(text):
    new_text = ''
    for character in text:
        if character == 'F':
            new_text += character + 'o'
        else:
            new_text += character
    return new_text