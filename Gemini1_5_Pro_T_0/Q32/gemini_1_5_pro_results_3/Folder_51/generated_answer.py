def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        if character == 'o':
            output_string = output_string + 'o' + 'O'
        else:
            output_string = output_string + character
    return output_string