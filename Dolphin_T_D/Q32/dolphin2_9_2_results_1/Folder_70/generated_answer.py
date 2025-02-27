def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        if char == 'P':
            output_string += char + 'V'
        else:
            output_string += char
    return output_string