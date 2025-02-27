def insert_before_character(input_string):
    output_string = ''
    for character in input_string:
        if character == '6':
            output_string += '9' + character
        else:
            output_string += character
    return output_string