def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        if character == 'w':
            output_string = output_string + 'wn'
        else:
            output_string = output_string + character
    return output_string