def insert_before_character(string):
    new_string = ''
    for character in string:
        if character == '2':
            new_string += 'S' + character
        else:
            new_string += character
    return new_string