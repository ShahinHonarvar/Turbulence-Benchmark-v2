def insert_after_character(input_string):
    new_string = ''
    for char in input_string:
        new_string += char
        if char == 'H':
            new_string += 's'
    return new_string