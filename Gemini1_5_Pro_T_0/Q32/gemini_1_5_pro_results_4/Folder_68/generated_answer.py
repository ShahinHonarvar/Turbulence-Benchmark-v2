def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        if character == 'i':
            output_string = output_string + 'i0'
        else:
            output_string = output_string + character
    return output_string