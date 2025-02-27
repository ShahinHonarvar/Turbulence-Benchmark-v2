def insert_after_character(input_string):
    new_string = ''
    for char in input_string:
        new_string += char
        if char == 'a':
            new_string += 'a'
    return new_string