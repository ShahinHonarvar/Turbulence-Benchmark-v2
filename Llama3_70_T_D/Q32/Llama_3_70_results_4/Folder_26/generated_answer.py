def insert_after_character(input_string):
    new_string = ''
    for char in input_string:
        new_string += char
        if char == 'r':
            new_string += 'w'
    return new_string