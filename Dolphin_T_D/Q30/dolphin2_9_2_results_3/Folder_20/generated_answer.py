def insert_before_character(input_string):
    output_string = ''
    for character in input_string:
        if character == 'C':
            output_string += 'H'
        output_string += character
    return output_string