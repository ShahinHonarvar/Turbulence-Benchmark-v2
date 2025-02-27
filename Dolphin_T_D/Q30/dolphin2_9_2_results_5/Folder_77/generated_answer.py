def insert_before_character(input_string):
    output_string = ''
    for c in input_string:
        if c == '9':
            output_string += 'h'
        output_string += c
    return output_string