def insert_after_character(input_string):
    output_string = ''
    for character in input_string:
        if character == '9':
            output_string = output_string + character + 'h'
        else:
            output_string = output_string + character
    return output_string