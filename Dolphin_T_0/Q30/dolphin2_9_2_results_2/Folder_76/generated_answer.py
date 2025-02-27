def insert_before_character(input_string):
    output_string = ''
    for c in input_string:
        if c == 'F':
            output_string += 'm' + c
        else:
            output_string += c
    return output_string