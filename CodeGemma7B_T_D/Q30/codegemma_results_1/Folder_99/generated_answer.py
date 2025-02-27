def insert_before_character(string):
    new_string = ''
    for character in string:
        if character == 'a':
            new_string += 'W' + character
        else:
            new_string += character
    return new_string