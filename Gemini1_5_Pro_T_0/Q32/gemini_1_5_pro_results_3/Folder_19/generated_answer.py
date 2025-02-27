def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        output_string += character
        if character == '5':
            output_string += 'h'
    return output_string