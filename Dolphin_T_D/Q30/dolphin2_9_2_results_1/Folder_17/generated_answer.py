def insert_before_character(input_string):
    new_string = ''
    for char in input_string:
        if char == 'Q':
            new_string += 'I' + char
        else:
            new_string += char
    return new_string