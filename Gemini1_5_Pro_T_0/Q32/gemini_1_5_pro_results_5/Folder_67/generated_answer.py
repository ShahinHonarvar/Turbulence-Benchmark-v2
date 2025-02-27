def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        output_string += character
        if character == 'j':
            output_string += '1'
    return output_string