def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        output_string += character
        if character == 'm':
            output_string += 'N'
    return output_string