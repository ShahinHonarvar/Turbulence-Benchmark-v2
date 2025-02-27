def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        output_string += character
        if character == 'A':
            output_string += 'A'
    return output_string