def insert_after_character(input_string):
    new_string = ''
    for char in input_string:
        new_string += char
        if char == ' ':
            new_string += 'K'
    return new_string