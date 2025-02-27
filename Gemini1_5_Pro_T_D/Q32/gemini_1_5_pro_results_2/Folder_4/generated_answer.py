def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        output_string += character
        if character == 'a':
            output_string += '6'
    return output_string