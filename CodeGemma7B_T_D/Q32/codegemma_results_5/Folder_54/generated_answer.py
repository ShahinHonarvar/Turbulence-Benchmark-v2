def insert_after_character(string):
    new_string = ''
    for character in string:
        if character == 'M':
            new_string += character + 'f'
        else:
            new_string += character
    return new_string