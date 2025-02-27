def insert_before_character(input_string):
    new_string = ''
    for char in input_string:
        if char == 'x':
            new_string += 'N' + char
        else:
            new_string += char
    return new_string