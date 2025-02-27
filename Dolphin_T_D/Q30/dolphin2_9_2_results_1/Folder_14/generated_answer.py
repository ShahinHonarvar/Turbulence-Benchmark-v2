def insert_before_character(text):
    new_text = ''
    for character in text:
        if character == ' ':
            new_text = new_text + ' ' + character
        else:
            new_text = new_text + character
    return new_text