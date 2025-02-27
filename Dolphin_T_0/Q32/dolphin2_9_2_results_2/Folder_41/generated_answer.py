def insert_after_character(string):
    new_string = ''
    for character in string:
        new_string += character
        if character == 'O':
            new_string += 'o'
    return new_string