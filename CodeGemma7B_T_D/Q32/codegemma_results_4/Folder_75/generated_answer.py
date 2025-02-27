def insert_after_character(text):
    updated_text = ''
    for character in text:
        if character == 'U':
            updated_text += character + 'q'
        else:
            updated_text += character
    return updated_text