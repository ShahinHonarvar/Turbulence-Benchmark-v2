def insert_before_character(input_string):
    modified_string = ''
    for char in input_string:
        if char == 'o':
            modified_string += '0' + char
        else:
            modified_string += char
    return modified_string