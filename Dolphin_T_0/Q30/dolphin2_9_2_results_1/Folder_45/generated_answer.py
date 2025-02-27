def insert_before_character(input_string):
    output_string = ''
    for character in input_string:
        if character == 'O':
            output_string += 'O' + character
        else:
            output_string += character
    return output_string