def insert_after_character(input_string):
    new_string = ''
    for char in input_string:
        if char == 'U':
            new_string += char + 'q'
        else:
            new_string += char
    return new_string