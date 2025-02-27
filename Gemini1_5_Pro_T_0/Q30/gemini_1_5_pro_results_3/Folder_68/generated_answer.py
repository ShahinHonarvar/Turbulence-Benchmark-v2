def insert_before_character(input_string):
    output_string = ''
    for character in input_string:
        if character == 'i':
            output_string += '0'
        output_string += character
    return output_string