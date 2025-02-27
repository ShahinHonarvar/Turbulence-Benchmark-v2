def insert_after_character(input_string):
    modified_string = ''
    for char in input_string:
        modified_string += char
        if char == 't':
            modified_string += 'G'
    return modified_string