def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        if character == 'E':
            output_string += 'Ef'
        else:
            output_string += character
    return output_string