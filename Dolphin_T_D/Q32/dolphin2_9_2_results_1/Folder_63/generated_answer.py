def insert_after_character(input_string):
    new_string = ''
    for char in input_string:
        if char == '5':
            new_string += char + 'R'
        else:
            new_string += char
    return new_string