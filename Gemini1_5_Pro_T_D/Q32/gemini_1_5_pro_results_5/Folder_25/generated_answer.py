def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        output_string += character
        if character == 'e':
            output_string += 'W'
    return output_string