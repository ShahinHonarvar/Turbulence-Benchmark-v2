def insert_before_character(input_string):
    new_string = ''
    for char in input_string:
        if char == 'H':
            new_string += 's' + char
        else:
            new_string += char
    return new_string