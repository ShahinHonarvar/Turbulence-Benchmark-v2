def insert_after_character(the_string):
    new_string = ''
    for character in the_string:
        if character == '6':
            new_string += character + '9'
        else:
            new_string += character
    return new_string