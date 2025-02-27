def insert_before_character(input_string):
    output_string = ''
    for character in input_string:
        if character == 't':
            output_string += 'Gt'
        else:
            output_string += character
    return output_string