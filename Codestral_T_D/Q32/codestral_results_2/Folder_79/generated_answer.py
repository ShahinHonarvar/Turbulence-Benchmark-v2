def insert_after_character(input_string):
    new_string = ''
    for char in input_string:
        new_string += char
        if char == 'E':
            new_string += 'E'
    return new_string