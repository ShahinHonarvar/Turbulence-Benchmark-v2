def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        output_string += char
        if char == 'm':
            output_string += 'Q'
    return output_string