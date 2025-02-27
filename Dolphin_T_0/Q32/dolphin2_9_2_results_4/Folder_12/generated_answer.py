def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'I':
            new_string += ' '
    return new_string