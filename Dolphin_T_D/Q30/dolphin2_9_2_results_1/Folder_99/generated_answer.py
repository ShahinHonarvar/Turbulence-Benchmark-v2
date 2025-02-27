def insert_before_character(input_string):
    modified_string = ''
    for char in input_string:
        if char == 'a':
            modified_string += 'W'
        modified_string += char
    return modified_string