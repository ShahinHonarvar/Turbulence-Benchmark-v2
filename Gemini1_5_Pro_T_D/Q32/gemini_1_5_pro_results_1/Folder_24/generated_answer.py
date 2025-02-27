def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        if character == '0':
            output_string += '04'
        else:
            output_string += character
    return output_string