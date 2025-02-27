def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        output_string += char
        if char == 'R':
            output_string += 'V'
    return output_string