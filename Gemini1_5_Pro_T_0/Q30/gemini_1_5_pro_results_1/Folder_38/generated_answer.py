def insert_before_character(input_string):
    output_string = ''
    for character in input_string:
        if character == 'X':
            output_string = output_string + '6'
        output_string = output_string + character
    return output_string