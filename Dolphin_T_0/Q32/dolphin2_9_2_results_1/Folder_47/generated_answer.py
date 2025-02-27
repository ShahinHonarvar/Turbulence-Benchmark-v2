def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        output_string += char
        if char == 'E':
            output_string += 'f'
    return output_string