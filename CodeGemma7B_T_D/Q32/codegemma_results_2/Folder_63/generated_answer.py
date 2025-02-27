def insert_after_character(input_string):
    updated_string = ''
    for char in input_string:
        if char == '5':
            updated_string += char + 'R'
        else:
            updated_string += char
    return updated_string