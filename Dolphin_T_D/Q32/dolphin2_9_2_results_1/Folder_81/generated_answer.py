def insert_after_character(string):
    new_string = ''
    for character in string:
        new_string += character
        if character == 'A':
            new_string += 'A'
    return new_string