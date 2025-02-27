def insert_after_character(string_input):
    new_string = ''
    for char in string_input:
        new_string += char
        if char == 'I':
            new_string += ' '
    return new_string